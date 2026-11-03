# Week 2 learning log: Containerize a 3-Tier App

## Day 1
- Image vs container: An image is a read-only blueprint holding the app, its libraries and a minimal OS. A container is a running copy of that image with its own small writable layer. One image can start many containers, like one recipe making many cakes.

- Docker group: The docker command talks to the Docker engine through a socket that only root and the docker group can use. Joining the group lets me run docker without typing sudo every time. Members of that group effectively have root power, which is fine on my own VM but not on a shared server.
