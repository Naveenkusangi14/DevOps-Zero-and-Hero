#METHOD ONE  Distroless

# Stage 1: Build stage
FROM node AS build

WORKDIR /app

# Copy package.json and package-lock.json if available
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY main.js ./

# Stage 2: Runtime stage
FROM gcr.io/distroless/nodejs

WORKDIR /app

# Copy the application and node_modules from the build stage
COPY --from=build /app /app

# Run the application using Node.js
CMD ["node", "main.js"]




#METHOD TWO FROME NODE

# # Use the official Node.js image as the base image
# FROM node:18

# # Set the working directory in the container
# WORKDIR /app

# # Copy package.json and package-lock.json first to leverage Docker cache for npm install
# COPY package*.json ./

# # Install application dependencies
# RUN npm install

# # Copy the rest of your application code to the container
# COPY . .

# # Expose the port your application will run on
# EXPOSE 8000

# # Define the command to run your application
# CMD [ "node", "main.js" ]


#METHOD TWO FROME  UBUNTU
# FROM ubuntu

# WORKDIR /app

# RUN apt update
# RUN apt install -y curl
# RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
# RUN apt upgrade -y
# RUN apt install -y nodejs


# COPY package.json ./
# COPY package-lock.json ./
# COPY main.js ./

# RUN npm install

# ENTRYPOINT ["node", "main.js"]