# Use the official Ubuntu base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and application code into the container
COPY requirements.txt /app/
COPY devops /app/devops

# Install Python and pip, then install Python dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install -r requirements.txt

# Set the working directory to the directory containing manage.py
WORKDIR /app/devops

# Set the entry point to Python 3 and provide default arguments
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
