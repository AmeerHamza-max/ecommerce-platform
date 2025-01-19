# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port
EXPOSE 5004

# Command to run the application
CMD ["python", "app.py"]
