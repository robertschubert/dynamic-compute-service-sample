# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY src/count_files.py .

# Run the script
CMD ["python", "count_files.py"]