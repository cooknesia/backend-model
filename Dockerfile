# Use official Python 3.9 image as base
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 3000 for the Flask app
EXPOSE 3000

# Set environment variable for Flask app (optional)
ENV FLASK_APP=app.py

# Run the app with gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
