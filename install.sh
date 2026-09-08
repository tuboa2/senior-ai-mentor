#!/usr/bin/env bash
# ==============================================================================
# One-Command Cross-Platform Installer for Senior AI Engineering Mentor
# Compatible with Linux and macOS
# ==============================================================================

set -e

BOLD="\033[1m"
CYAN="\033[36m"
GREEN="\033[32m"
YELLOW="\033[33m"
RED="\033[31m"
RESET="\033[0m"

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

# 2. Install package locally or in editable mode
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo -e "${CYAN}Registering senior-ai-mentor package...${RESET}"

if python3 -m pip --version &>/dev/null; then
    # Try normal pip install, then --break-system-packages (for Debian/Ubuntu PEP 668)
    python3 -m pip install -e "$SCRIPT_DIR" --no-deps 2>/dev/null || \
    python3 -m pip install -e "$SCRIPT_DIR" --no-deps --break-system-packages 2>/dev/null || \
    echo -e "${YELLOW}[!] Note: pip installation skipped due to OS environment constraints; using direct executable links.${RESET}"
fi

# 3. Create user binary wrapper in ~/.local/bin
mkdir -p "$HOME/.local/bin"
cat << 'EOF' > "$HOME/.local/bin/mentor"
#!/usr/bin/env bash
python3 -m senior_mentor.cli "$@"
EOF
cat << 'EOF' > "$HOME/.local/bin/agy-mentor"
#!/usr/bin/env bash
python3 -m senior_mentor.cli "$@"
EOF
chmod +x "$HOME/.local/bin/mentor" "$HOME/.local/bin/agy-mentor"
echo -e "${GREEN}✓ Created global CLI commands: $HOME/.local/bin/mentor & agy-mentor${RESET}"

# 4. Initialize global persistence and Antigravity configuration
echo -e "${CYAN}Configuring global Antigravity integration and shared memory...${RESET}"
python3 -m senior_mentor.cli init

echo -e "\n${BOLD}${GREEN}=================================================================${RESET}"
echo -e "${BOLD}${GREEN}            INSTALLATION COMPLETED SUCCESSFULLY!                 ${RESET}"
echo -e "${BOLD}${GREEN}=================================================================${RESET}"
echo -e "${BOLD}How to use:${RESET}"
echo -e "  1. In any project terminal: ${CYAN}mentor init${RESET} (activates mentor in that repo)"
echo -e "  2. Interactive mentor chat:  ${CYAN}mentor${RESET}"
echo -e "  3. Check competency status:  ${CYAN}mentor --status${RESET}"
echo -e "  4. Mock interview:           ${CYAN}mentor --interview system_design${RESET}"
echo -e "  5. In Antigravity IDE/CLI:   Open any workspace and start chatting with the Council!\n"
