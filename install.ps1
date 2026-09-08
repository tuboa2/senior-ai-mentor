# ==============================================================================
# One-Command Windows PowerShell Installer for Senior AI Engineering Mentor
# ==============================================================================

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "     INSTALLING SENIOR AI ENGINEERING MENTOR ENVIRONMENT         " -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

# 1. Verify Python version
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue
}

if (-not $pythonCmd) {
    Write-Host "[ERROR] Python was not found in PATH. Please install Python 3.10+." -ForegroundColor Red
    Exit 1
}

$pyVer = & $pythonCmd.Source -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
Write-Host "Detected Python version: $pyVer" -ForegroundColor Green

# 2. Install package in editable mode
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Installing senior-ai-mentor package..." -ForegroundColor Cyan

& $pythonCmd.Source -m pip install -e $scriptDir --no-deps

# 3. Initialize global persistence and Antigravity configuration
Write-Host "Configuring global Antigravity integration and shared memory..." -ForegroundColor Cyan
& $pythonCmd.Source "$scriptDir\senior_mentor\cli.py" init

Write-Host ""
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "            INSTALLATION COMPLETED SUCCESSFULLY!                 " -ForegroundColor Green
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "How to use:"
Write-Host "  1. In any project terminal: mentor init" -ForegroundColor Yellow
Write-Host "  2. Interactive mentor chat:  mentor" -ForegroundColor Yellow
Write-Host "  3. Check competency status:  mentor --status" -ForegroundColor Yellow
Write-Host "  4. Mock interview:           mentor --interview system_design" -ForegroundColor Yellow
Write-Host "  5. In Antigravity: Open your workspace and chat with the Council!`n" -ForegroundColor Yellow
