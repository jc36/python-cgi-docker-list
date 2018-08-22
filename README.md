A simple web application.
List running Docker-containers.
docker run -d -p 8000:8000 --volume /var/run/docker.sock:/var/run/docker.sock --privileged jc36/python-cgi-docker-list
