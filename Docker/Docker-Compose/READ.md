Docker Compose Commands Cheat Sheet


Docker: Get Docker
Docker Compose: Get Docker Compose
Docker Compose Commands
1. docker-compose up
Starts and runs the services defined in the docker-compose.yml file. If the necessary images are not found locally, Docker will pull them from the registry.

bash
Copy code
docker-compose up
-d: Run containers in detached mode (in the background).
bash
Copy code
docker-compose up -d
2. docker-compose down
Stops and removes containers, networks, volumes, and images created by docker-compose up.

bash
Copy code
docker-compose down
--volumes: Remove named volumes declared in the volumes section of docker-compose.yml.
bash
Copy code
docker-compose down --volumes
3. docker-compose build
Builds the services defined in docker-compose.yml. This is useful when Dockerfiles are modified or images need to be rebuilt.

bash
Copy code
docker-compose build
--no-cache: Rebuilds images without using the cache.
bash
Copy code
docker-compose build --no-cache
4. docker-compose pull
Pulls the latest version of the images defined in the docker-compose.yml file from the Docker registry.

bash
Copy code
docker-compose pull
5. docker-compose ps
Lists the status of containers associated with the Docker Compose project.

bash
Copy code
docker-compose ps
6. docker-compose stop
Stops all running containers without removing them.

bash
Copy code
docker-compose stop
7. docker-compose start
Starts services that were stopped with docker-compose stop without recreating containers.

bash
Copy code
docker-compose start
8. docker-compose restart
Restarts all containers.

bash
Copy code
docker-compose restart
9. docker-compose logs
Shows the logs of all running services.

bash
Copy code
docker-compose logs
-f: Follows log output.
bash
Copy code
docker-compose logs -f
10. docker-compose exec
Executes a command inside a running service container.

bash
Copy code
docker-compose exec <service_name> <command>
Example:

bash
Copy code
docker-compose exec mongodb bash
11. docker-compose config
Validates and displays the Compose file in a canonical format.

bash
Copy code
docker-compose config
12. docker-compose top
Displays the running processes inside your containers.

bash
Copy code
docker-compose top
13. docker-compose rm
Removes stopped service containers. This is useful after docker-compose down if you want to clean up the stopped containers.

bash
Copy code
docker-compose rm
-f: Forces removal without confirmation.
bash
Copy code
docker-compose rm -f
14. docker-compose scale
Scales the number of containers for a specific service.

bash
Copy code
docker-compose scale <service_name>=<number_of_containers>
Example:

bash
Copy code
docker-compose scale mongodb=3
15. docker-compose version
Displays the version of Docker Compose.

bash
Copy code
docker-compose version
