

# Use an official Python image to build the application
FROM python:3.9-slim AS build

# Set working directory
WORKDIR /app

# Copy the application files to the container
COPY calcalator.py ./

# Install dependencies (if any)
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

############################################
# HERE STARTS THE MAGIC OF MULTI STAGE BUILD
############################################

# Use a minimal Python image for the final stage
FROM gcr.io/distroless/python3

# Set working directory
WORKDIR /app

# Copy the Python script and any dependencies from the build stage
COPY --from=build /app /app

# Set the command to run the Python application
CMD ["calcalator.py"]
