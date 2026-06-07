@echo off
set GIT="C:\Users\u\AppData\Local\GitHubDesktop\app-3.5.12\resources\app\git\cmd\git.exe"
set TEMP_REPO=%TEMP%\leamouawad-restore
set DEST=C:\Users\u\Documents\Claude\Projects\Portfolio\index.html

echo Cloning repo...
if exist %TEMP_REPO% rmdir /s /q %TEMP_REPO%
%GIT% clone https://github.com/LeaMouawad/leamouawad.github.io.git %TEMP_REPO%

echo Restoring index.html from GitHub...
copy /Y "%TEMP_REPO%\index.html" "%DEST%"

echo.
echo Done! index.html has been restored from GitHub.
pause
