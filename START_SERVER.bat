@echo off
echo ================================
echo   Portfolio Local Server
echo ================================
echo.
echo Your computer's IP address:
ipconfig | findstr /i "IPv4"
echo.
echo Open your phone browser and go to:
echo   http://[YOUR IP ABOVE]:8080
echo.
echo Keep this window open while testing.
echo Press Ctrl+C to stop the server.
echo.
cd /d "%~dp0"
python -m http.server 8080
pause
