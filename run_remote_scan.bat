@echo off
REM run_remote_scan.bat - clone a remote repo shallowly, run the scanner, copy CSV out, and clean up
REM Usage: run_remote_scan.bat <git-repo-url> [output_csv]

if "%~1"=="" (
  echo Usage: %~nx0 ^<git-repo-url^> [output_csv]
  exit /b 2
)

set "REPO_URL=%~1"

if "%~2"=="" (
  set "OUT=%CD%\missing_activities_%RANDOM%.csv"
) else (
  set "OUT=%~2"
)

set "SCRIPT_DIR=%~dp0"
set "SCANNER=%SCRIPT_DIR%scan_missing_activities.py"

if not exist "%SCANNER%" (
  echo Scanner not found at "%SCANNER%"
  exit /b 3
)

where git >nul 2>&1 || (
  echo git not found
  exit /b 3
)

REM find python or python3
where python >nul 2>&1
if %ERRORLEVEL%==0 (
  set "PY_CMD=python"
) else (
  where python3 >nul 2>&1
  if %ERRORLEVEL%==0 (
    set "PY_CMD=python3"
  ) else (
    echo python not found
    exit /b 3
  )
)

# If first arg starts with - or is an existing file, forward all args to the scanner
set "FIRST=%~1"
set "FIRSTCHAR=%FIRST:~0,1%"
if "%FIRSTCHAR%"=="-" (
  "%PY_CMD%" "%SCANNER%" %*
  exit /b %ERRORLEVEL%
)
if exist "%~1" (
  "%PY_CMD%" "%SCANNER%" %*
  exit /b %ERRORLEVEL%
)

set "TMP_DIR=%TEMP%\scanrepo_%RANDOM%_%RANDOM%"
mkdir "%TMP_DIR%"

echo Cloning %REPO_URL% (shallow) into %TMP_DIR%...
git clone --depth 1 "%REPO_URL%" "%TMP_DIR%" || (
  echo git clone failed
  rd /s /q "%TMP_DIR%"
  exit /b 4
)

echo Running scanner...
"%PY_CMD%" "%SCANNER%" --single-output "%OUT%" "%TMP_DIR%" || (
  echo scanner failed
  rd /s /q "%TMP_DIR%"
  exit /b 5
)

echo Result written to: %OUT%
rd /s /q "%TMP_DIR%"
exit /b 0
