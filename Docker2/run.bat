@echo off
echo Building Docker image...
docker build -t my-app .

echo Starting the container...
docker run -p 5000:5000 my-app

pause 