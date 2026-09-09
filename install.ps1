# ==============================================================================
# One-Command Windows PowerShell Installer for Senior AI Engineering Mentor
# Repository: https://github.com/tuboa2/senior-ai-mentor
# ==============================================================================

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "  INSTALLING SENIOR AI ENGINEERING MENTOR FOR ANTIGRAVITY CLI    " -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

# 1. Verify Python version (>= 3.10)
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

# 2. Determine source repository directory
$repoUrl = "https://github.com/tuboa2/senior-ai-mentor.git"
$installDir = Join-Path $HOME ".senior-ai-mentor"
$sourceDir = ""

if ($PSScriptRoot -and (Test-Path (Join-Path $PSScriptRoot "senior_mentor\cli.py"))) {
    $sourceDir = $PSScriptRoot
} elseif ($MyInvocation.MyCommand.Path -and (Test-Path (Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) "senior_mentor\cli.py"))) {
    $sourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path
} else {
    Write-Host "Cloning / updating repository in $installDir..." -ForegroundColor Cyan
    if (Test-Path (Join-Path $installDir ".git")) {
        git -C $installDir pull --quiet
    } else {
        git clone --depth=1 $repoUrl $installDir
    }
    $sourceDir = $installDir
}

Write-Host "Installing senior-ai-mentor package from $sourceDir..." -ForegroundColor Cyan

# 3. Install package with pip
& $pythonCmd.Source -m pip install -e $sourceDir --no-deps

# 4. Initialize global persistence and Antigravity configuration
Write-Host "Configuring global Antigravity integration and shared memory..." -ForegroundColor Cyan
$env:ANTIGRAVITY_CLI = "1"
$cliPath = Join-Path $sourceDir "senior_mentor\cli.py"
& $pythonCmd.Source $cliPath init

Write-Host ""
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "            INSTALLATION COMPLETED SUCCESSFULLY!                 " -ForegroundColor Green
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "How to use (Strictly Antigravity CLI Environment):"
Write-Host "  1. Launch Antigravity CLI in your project repository: agy" -ForegroundColor Cyan
Write-Host "  2. The 14-member Expert Council is active automatically in agy!" -ForegroundColor Cyan
Write-Host "  3. Use slash commands directly in your agy chat session:" -ForegroundColor Cyan
Write-Host "     - /council <topic>      : Deliberate technical trade-offs without false compromise" -ForegroundColor Yellow
Write-Host "     - /mentor <query>       : Adaptive Socratic scaffolding (L3-L5)" -ForegroundColor Yellow
Write-Host "     - /solve <query>        : Direct production code and derivations (L0-L2)" -ForegroundColor Yellow
Write-Host "     - /interview [domain]   : Realistic senior/staff mock technical interview" -ForegroundColor Yellow
Write-Host "     - /status               : View learner profile & competency metrics" -ForegroundColor Yellow
Write-Host "     - /hint                 : Progressive concept clues" -ForegroundColor Yellow
Write-Host "     - /challenge <concept>  : Isomorphic concept challenge" -ForegroundColor Yellow
Write-Host "     - /refine               : Autonomous self-improvement proposals" -ForegroundColor Yellow
Write-Host "  4. To configure an existing workspace: agy-mentor init" -ForegroundColor Cyan
Write-Host "  5. CLI helper flags: agy-mentor --status or agy-mentor --skills`n" -ForegroundColor Cyan
Write-Host "Note: Standalone terminal REPL is disabled. Pair programming is hosted strictly inside 'agy'.`n" -ForegroundColor Magenta
