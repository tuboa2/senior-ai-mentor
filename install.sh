#!/usr/bin/env bash
# ==============================================================================
# One-Command Cross-Platform Installer for Senior AI Engineering Mentor
# Compatible with Linux and macOS
# Repository: https://github.com/tuboa2/senior-ai-mentor
# ==============================================================================

set -e

BOLD="\033[1m"
CYAN="\033[36m"
GREEN="\033[32m"
YELLOW="\033[33m"
RED="\033[31m"
RESET="\033[0m"

REPO_URL="https://github.com/tuboa2/senior-ai-mentor.git"
INSTALL_DIR="$HOME/.senior-ai-mentor"

echo -e "${BOLD}${CYAN}=================================================================${RESET}"
echo -e "${BOLD}${CYAN}     INSTALLING SENIOR AI ENGINEERING MENTOR ENVIRONMENT         ${RESET}"
echo -e "${BOLD}${CYAN}=================================================================${RESET}"

# 1. Verify Python version (>= 3.10)
if ! command -v python3 &>/dev/null; then
    echo -e "${RED}[ERROR] python3 is not installed or not in PATH. Please install Python 3.10+ first.${RESET}"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)')
PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 10 ]); then
    echo -e "${RED}[ERROR] Python 3.10 or higher is required. Found Python ${PYTHON_VERSION}.${RESET}"
    exit 1
fi

echo -e "${GREEN}✓ Detected Python ${PYTHON_VERSION}${RESET}"

# 2. Determine target source directory
SOURCE_DIR=""
if [ -n "${BASH_SOURCE[0]}" ] && [ -f "${BASH_SOURCE[0]}" ]; then
    CURRENT_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    if [ -f "$CURRENT_SCRIPT_DIR/senior_mentor/cli.py" ] && [ -f "$CURRENT_SCRIPT_DIR/pyproject.toml" ]; then
        SOURCE_DIR="$CURRENT_SCRIPT_DIR"
    fi
fi

if [ -z "$SOURCE_DIR" ]; then
    echo -e "${CYAN}Cloning / updating repository in $INSTALL_DIR...${RESET}"
    if [ -d "$INSTALL_DIR/.git" ]; then
        git -C "$INSTALL_DIR" pull --quiet || true
    else
        git clone --depth=1 "$REPO_URL" "$INSTALL_DIR"
    fi
    SOURCE_DIR="$INSTALL_DIR"
else
    echo -e "${CYAN}Installing from local repository: $SOURCE_DIR${RESET}"
fi

# 3. Register package with pip (with PEP 668 fallback)
echo -e "${CYAN}Registering senior-mentor package...${RESET}"
if python3 -m pip --version &>/dev/null; then
    python3 -m pip install -e "$SOURCE_DIR" --no-deps 2>/dev/null || \
    python3 -m pip install -e "$SOURCE_DIR" --no-deps --break-system-packages 2>/dev/null || \
    echo -e "${YELLOW}[!] Note: pip installation skipped due to system constraints; using direct wrapper execution.${RESET}"
fi

# 4. Create user binary wrappers in ~/.local/bin
mkdir -p "$HOME/.local/bin"

cat << 'INNER_EOF' > "$HOME/.local/bin/mentor"
#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -d "$HOME/.senior-ai-mentor" ]; then
    export PYTHONPATH="$HOME/.senior-ai-mentor:$PYTHONPATH"
fi
exec python3 -m senior_mentor.cli "$@"
INNER_EOF

cat << 'INNER_EOF' > "$HOME/.local/bin/agy-mentor"
#!/usr/bin/env bash
if [ -d "$HOME/.senior-ai-mentor" ]; then
    export PYTHONPATH="$HOME/.senior-ai-mentor:$PYTHONPATH"
fi
exec python3 -m senior_mentor.cli "$@"
INNER_EOF

# If installing from a specific custom source dir, update wrappers to include that path
sed -i "s|\$HOME/\.senior-ai-mentor|$SOURCE_DIR|g" "$HOME/.local/bin/mentor" "$HOME/.local/bin/agy-mentor"

chmod +x "$HOME/.local/bin/mentor" "$HOME/.local/bin/agy-mentor"
echo -e "${GREEN}✓ Created executable CLI commands: $HOME/.local/bin/mentor and agy-mentor${RESET}"

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo -e "${YELLOW}[!] Recommendation: Add ~/.local/bin to your PATH in ~/.bashrc or ~/.zshrc:${RESET}"
    echo -e "    export PATH=\"\$HOME/.local/bin:\$PATH\""
fi

# 5. Initialize global persistence and Antigravity configuration
echo -e "${CYAN}Configuring global Antigravity integration and shared memory...${RESET}"
PYTHONPATH="$SOURCE_DIR:$PYTHONPATH" python3 -m senior_mentor.cli init

echo -e "\n${BOLD}${GREEN}=================================================================${RESET}"
echo -e "${BOLD}${GREEN}            INSTALLATION COMPLETED SUCCESSFULLY!                 ${RESET}"
echo -e "${BOLD}${GREEN}=================================================================${RESET}"
echo -e "${BOLD}How to use:${RESET}"
echo -e "  1. In any project workspace: ${CYAN}mentor init${RESET} (configures local repo & connects to global memory)"
echo -e "  2. Interactive mentor REPL:  ${CYAN}mentor${RESET}"
echo -e "  3. Check competency status:  ${CYAN}mentor --status${RESET}"
echo -e "  4. Mock interview session:   ${CYAN}mentor --interview system_design${RESET}"
echo -e "  5. In Antigravity IDE/CLI:   Open any project and chat with the 14-member Council!\n"
