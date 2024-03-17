# Use the official Python image as base
FROM python:3.9

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Clone the repository
RUN git clone https://github.com/saad-codes/real_time_streaming.git .

# Install Flask and MySQL client library
RUN pip install Flask mysql-connector-python

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
