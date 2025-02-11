@echo off
setlocal enabledelayedexpansion

:: Check if Resolve is installed
set "RESOLVE_INSTALL_DIR=C:\Program Files\Blackmagic Design\DaVinci Resolve"
if not exist "%RESOLVE_INSTALL_DIR%" (
    echo DaVinci Resolve installation not found at:
    echo %RESOLVE_INSTALL_DIR%
    echo Please install DaVinci Resolve before running this script.
    echo.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

:: Set paths
set "INSTALLER_DIR=%~dp0scripts"
set "SCRIPTS_DIR=%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts"
set "PYRESOLVE_DIR=%SCRIPTS_DIR%\Utility"

:: Check if source scripts exist
if not exist "%INSTALLER_DIR%" (
    echo ERROR: Scripts folder not found at:
    echo %INSTALLER_DIR%
    echo Please ensure the scripts folder exists next to this installer.
    echo.
    echo Press any key to exit...
    pause >nul
    exit /b 1
)

:: Create PyResolve directory if it doesn't exist
if not exist "%PYRESOLVE_DIR%" (
    mkdir "%PYRESOLVE_DIR%" 2>nul
    if errorlevel 1 (
        echo ERROR: Failed to create directory: %PYRESOLVE_DIR%
        echo Make sure you have administrator rights to create folders in ProgramData.
        goto :error
    )
)

:: Copy all files from source to destination
xcopy /Y /E /I "%INSTALLER_DIR%\*" "%PYRESOLVE_DIR%" >nul
if errorlevel 1 (
    echo ERROR: Failed to copy files to %PYRESOLVE_DIR%
    echo Make sure you have administrator rights.
    goto :error
)

echo.
echo Installation completed successfully!
echo Scripts have been installed to:
echo %PYRESOLVE_DIR%
echo.
echo Press any key to exit...
pause >nul
exit /b 0

:error
echo.
echo Installation failed!
echo.
echo Press any key to exit...
pause >nul
exit /b 1