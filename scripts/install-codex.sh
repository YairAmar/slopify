#!/usr/bin/env bash
# 🚀✨ Slopify for Codex — one-command install 💯🔥
# Installs the WHOLE slop skill stack (slop-mode, ununslop, antiprinciple-*,
# setup-slopify, slopify-help) + the /prompts:slopify alias into ~/.codex.
# The skills/ tree is the single source of truth, shared with the Claude plugin.
# Always-on AGENTS.md is OPT-IN (see the note at the end).
set -euo pipefail

CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "🎨 Installing the Slopify skill stack into ${CODEX_HOME} ..."
mkdir -p "${CODEX_HOME}/skills" "${CODEX_HOME}/prompts"

count=0
for dir in "${HERE}"/skills/*/; do
  name="$(basename "$dir")"
  mkdir -p "${CODEX_HOME}/skills/${name}"
  cp -R "${dir}." "${CODEX_HOME}/skills/${name}/"
  echo "  ✅ ${name}"
  count=$((count + 1))
done
cp "${HERE}/codex/prompts/slopify.md" "${CODEX_HOME}/prompts/slopify.md"

echo
echo "✅ ${count} slop skills installed under ${CODEX_HOME}/skills/"
echo "✅ Alias installed:  ${CODEX_HOME}/prompts/slopify.md  (use /prompts:slopify)"
echo
echo "🤿 Start a NEW Codex session, then:"
echo "     \$slop-mode           # enter the full slop experience"
echo "     \$ununslop            # just the prose rulebook"
echo "     /prompts:slopify      # same slop, via the alias"
echo
echo "🌊 Want ALWAYS-ON slop in every message? Append the standing orders:"
echo "     cat '${HERE}/codex/AGENTS.md' >> '${CODEX_HOME}/AGENTS.md'"
echo
echo "🥳 Done! Make your agent say less, with more! 💯🔥🌈"
