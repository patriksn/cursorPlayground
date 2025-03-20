# Docker Flask Application

A basic Flask application containerized with Docker.

## Setup

1. Build the Docker image:
```bash
docker build -t flask-app .
```

2. Run the container:
```bash
docker run -p 5000:5000 flask-app
```

## Accessing the Application

Once the container is running, you can access the application at:
```
http://localhost:5000
```

## Project Structure

- `app.py`: Main Flask application
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration
- `.dockerignore`: Files to exclude from the container
- `README.md`: This file

## Development

To modify the application:
1. Edit `app.py`
2. Rebuild the container
3. Run the new container 