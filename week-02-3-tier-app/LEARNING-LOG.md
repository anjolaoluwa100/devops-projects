# Week 2 learning log: Containerize a 3-Tier App

## Day 1
- Image vs container: An image is a read-only blueprint holding the app, its libraries and a minimal OS. A container is a running copy of that image with its own small writable layer. One image can start many containers, like one recipe making many cakes.

- Docker group: The docker command talks to the Docker engine through a socket that only root and the docker group can use. Joining the group lets me run docker without typing sudo every time. Members of that group effectively have root power, which is fine on my own VM but not on a shared server.

## Day 2
- `-d` (detached): runs the container in the background, so my terminal stays free.
- `-p 8081:80`: publishes a port. Requests to port 8081 on the VM go to port 80 inside the container (HOST:CONTAINER).
- `docker exec -it web sh`: opens a shell inside a running container. `-it` makes it interactive, and `sh` is the shell.
- Deleting a container doesn't delete its image. `nginx:alpine` was still in `docker images`, so I could start a new container from it straight away without downloading anything.
- Ran the API without Docker first, against a throwaway Postgres container, so any later bug will be a Docker problem, not a code problem. The app must listen on 0.0.0.0 to be reachable from outside.
