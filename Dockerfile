# Use the official Python image as base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and MySQL client library
RUN pip install Flask mysql-connector-python

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
