#!/usr/bin/env bash
#
# Mechanical half of SCRUB-CHECKLIST.md. Prints file:line for every marker hit
# so a human can review them.
#
# THIS IS A WORKLIST, NOT A VERDICT.
#   A hit is not automatically a failure — plenty are legitimate industry
#   reference. A clean run is not a pass — rules 1–4 are read by a human either
#   way. The exit code reflects "were there hits", never "is this publishable".
#
# Usage:  ./scripts/scrub-scan.sh skills/<skill-name> [more paths...]
#         ./scripts/scrub-scan.sh --quiet skills/ddex-delivery   # counts only

set -uo pipefail

PATTERNS="$(dirname "$0")/scrub-patterns.txt"
QUIET=0
[[ "${1:-}" == "--quiet" ]] && { QUIET=1; shift; }

if [[ $# -eq 0 ]]; then
  echo "usage: $0 [--quiet] <path> [path...]" >&2
  exit 2
fi
if [[ ! -f "$PATTERNS" ]]; then
  echo "scrub-scan: pattern file not found: $PATTERNS" >&2
  exit 2
fi

total=0
section=""

while IFS= read -r line; do
  # A CRLF pattern file (e.g. a Windows checkout) leaves a trailing \r, which
  # turns every blank line into a pattern that matches everything.
  line="${line%$'\r'}"
  # Section headers become report headings
  if [[ "$line" =~ ^#[[:space:]]*──.*·[[:space:]]*(.*)[[:space:]]*── ]]; then
    section="${BASH_REMATCH[1]}"
    continue
  fi
  [[ -z "$line" || "$line" == \#* ]] && continue

  hits="$(grep -rInE --binary-files=without-match "$line" "$@" 2>/dev/null || true)"
  [[ -z "$hits" ]] && continue

  count="$(printf '%s\n' "$hits" | grep -c . || true)"
  total=$(( total + count ))

  if [[ $QUIET -eq 0 ]]; then
    printf '\n\033[1m%s\033[0m  \033[2m(%s hits)\033[0m\n' "${section:-uncategorised}" "$count"
    printf '  pattern: %s\n' "$line"
    printf '%s\n' "$hits" | sed 's/^/    /'
  fi
done < "$PATTERNS"

printf '\n'
if [[ $total -eq 0 ]]; then
  printf '\033[2mscrub-scan: 0 marker hits across %s path(s).\033[0m\n' "$#"
  printf '\033[2mA clean scan is NOT a pass — read rules 1–4 in SCRUB-CHECKLIST.md.\033[0m\n'
else
  printf '\033[1mscrub-scan: %s marker hits to review.\033[0m\n' "$total"
  printf 'Each hit needs a decision: remove, rewrite as generic industry reference,\n'
  printf 'or justify in the PR. Record the outcome in the sign-off block.\n'
fi

# Exit 0 always: this is a worklist, and a non-zero exit would invite someone to
# wire it into CI as a pass/fail gate, which is exactly the misreading the
# checklist warns against.
exit 0
