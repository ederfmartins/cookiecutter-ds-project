# Running the {{ cookiecutter.repo_name }} environment in docker

## Install the requirements

- **Docker** - https://docs.docker.com/installation/
- **Docker-Compose** - https://docs.docker.com/compose/install/ (Get version 1.4.2; *e.g.,* pip install docker-compose==1.4.2)


## Pull the docker images

    $ docker pull catholabs/elastic-with-marvel
    $ docker pull redis

# Running with docker compose

At **deploy/local** directory (RECOMMENDED, run only what you need)  

    $ sudo docker-compose -f docker/docker-compose.yml up redis elastic

 If everything runs well you will be able to access the services using your host machine.

 Open the browser and hit [http://localhost:9200](http://localhost:9200)

## Attaching to a running container

If you need to attach to a shell on some running container you can do this using **attach** and specifying the command to run

    $ docker  -i -t <container_name> /bin/bash

> -i to enter in interactive mode and -t to open a TTY, once inside the shell maybe you will need to export TERM variable ``export TERM=xterm``

#### Run the script and exit

    $ docker run --rm <container_name> <command>

## Troubleshooting

### Kill containers
If you run ``docker ps`` and there is a lot of running containers

    $ docker rm $(docker kill $(docker ps -aq))

### Remove images
If you want to remove all the local images to download again

    $ docker rmi $(docker images -aq)

 > You can pass -f to force
 
### Inspect

You can inspect the state of a running container using ``docker inspect``

https://docs.docker.com/reference/commandline/inspect/


## Docker compose environment

Inside the ``/deploy/local`` folder there is a file called ``docker-compose.yml`` and a folders containing the repositories for **elasticsearch** and **redis** data.

docker-compose will define different containers for the project

- redis
   - based in the official redis image and expose redis ports
   - will persist data under ``deploy/local/redisdata``
- elastic
   - based in the official elasticsearch image and expose ES ports.
   - will persist data under ``deploy/local/es/data``
- notebook
   - based in jupyter/scipy-notebook
   - run Jupyter on 8888
