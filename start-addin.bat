@echo off
echo =============================================
echo  KI Mail Assistent - Outlook Add-in Server
echo =============================================
echo.
echo Starte HTTPS-Server auf https://localhost:3000
echo.
python "%~dp0server.py"
pause
