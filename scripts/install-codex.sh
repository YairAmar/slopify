#!/usr/bin/env bash
# 🚀✨ Slopify for Codex — one-command install 💯🔥
# Installs the ununslop skill + /prompts:slopify alias into ~/.codex.
# Always-on AGENTS.md is OPT-IN (see the note at the end).
set -euo pipefail

CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "🎨 Installing Slopify into ${CODEX_HOME} ..."
mkdir -p "${CODEX_HOME}/skills/ununslop" "${CODEX_HOME}/prompts"

cp "${HERE}/codex/skills/ununslop/SKILL.md" "${CODEX_HOME}/skills/ununslop/SKILL.md"
cp "${HERE}/codex/prompts/slopify.md"      "${CODEX_HOME}/prompts/slopify.md"

echo "✅ Skill installed:  ${CODEX_HOME}/skills/ununslop/SKILL.md"
echo "✅ Alias installed:  ${CODEX_HOME}/prompts/slopify.md  (use /prompts:slopify)"
echo
echo "🤿 Start a NEW Codex session, then:"
echo "     \$ununslop            # invoke the skill explicitly"
echo "     /prompts:slopify      # same slop, via the alias"
echo
echo "🌊 Want ALWAYS-ON slop in every message? Append the standing orders:"
echo "     cat '${HERE}/codex/AGENTS.md' >> '${CODEX_HOME}/AGENTS.md'"
echo
echo "🥳 Done! Make your agent say less, with more! 💯🔥🌈"
