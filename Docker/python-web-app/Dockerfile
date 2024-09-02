FROM ubuntu

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt and devops directory to /app
COPY requirements.txt /app
COPY devops /app/devops

# Install Python and pip, then install the Python dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install -r requirements.txt

# Set the working directory to /app/devops
WORKDIR /app/devops

# Specify the entry point and command to run the application
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
