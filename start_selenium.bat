@echo off
setlocal

set SELENIUM_SERVER_JAR=selenium-server-4.8.0.jar

:loop
echo Starting Selenium server...
taskkill /im java.exe /f > nul 2>&1
java -jar %SELENIUM_SERVER_JAR% standalone

echo Selenium server has stopped.
echo Restarting in 5 seconds...

ping 127.0.0.1 -n 6 > nul

echo Starting new Selenium server in a new command prompt...
start cmd /k java -jar %SELENIUM_SERVER_JAR% standalone

goto loop