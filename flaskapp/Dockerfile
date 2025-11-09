# Start from a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application
COPY . /app/

# Expose port 8000 (matches your app.py)
EXPOSE 8000

# Command to run the Flask app
CMD ["python", "app.py"]


