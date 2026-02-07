@echo off
REM Setup script for KentAI on Windows

echo Setting up KentAI...
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is required
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

REM Install dependencies
echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

REM Create .env if it doesn't exist
if not exist .env (
    echo Creating .env file...
    copy .env.example .env
    echo Created .env - customize it for your system
)

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Install Ollama: https://ollama.ai
echo 2. Run: ollama serve
echo 3. Pull a model: ollama pull llama2
echo 4. (Optional) Edit .env to customize app paths
echo 5. Run KentAI: python kent.py
echo.
echo Or try the demo without Ollama:
echo   python demo.py
echo.
pause
