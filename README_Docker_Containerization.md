# Docker Containerization for Flask Project

This document provides steps to containerize the Flask backend project using Docker.

## Prerequisites

- Docker installed on your machine. Download from https://www.docker.com/get-started

## Steps to Build and Run the Docker Container

1. Open a terminal and navigate to the project root directory (where the Dockerfile is located).

2. Build the Docker image:

```bash
docker build -t flask-backend .
```

3. Run the Docker container:

```bash
docker run -d -p 3000:3000 --name flask-backend-container flask-backend
```

- This maps port 3000 of the container to port 3000 on your host machine.
- The app will be accessible at http://localhost:3000

4. To stop the container:

```bash
docker stop flask-backend-container
```

5. To remove the container:

```bash
docker rm flask-backend-container
```

## Notes

- The Dockerfile uses the official Python 3.9 slim image.
- All dependencies from `requirements.txt` are installed.
- The entire project directory is copied into the container, including the `model/` directory with TensorFlow model files.
- The app runs with Gunicorn for production readiness.
- If you use environment variables, consider adding a `.env` file and passing it to the container with `--env-file` option in `docker run`.
- You can extend the Dockerfile or use docker-compose if you want to add more services like a database.

## Troubleshooting

- If you encounter issues with TensorFlow or other dependencies, ensure your Docker environment supports the required system libraries.
- For development, you can modify the Dockerfile to enable hot reloading or use volumes to mount source code.

This containerization will help you deploy and run your Flask backend consistently across different environments.
