# Docker Commands

1. install docker on your computer

    https://docs.docker.com/

2. Get docker image

    docker pull dalverse/all-spark-notebook

4. Prepare a folder to share with docker

    for example, on my computer is
    /Users/hongzhaozhu/workfiles/dockerShare

3. Start Docker Container

    docker run -v /Users/hongzhaozhu/workfiles/dockerShare:/home/dal/work -d -P dalverse/all-spark-notebook
    docker start containerID

4. Check docker running status

  - To see all images: docker images
  - To see all runnning containers: docker ps -a
  - docker logs containerID


5. Login container and view IP addr

  - docker exec -it containerID ip addr
  - docker exec -it --user root containerID bash

6. Log in jupyter notebook with spark

    use "docker logs containerID" to see the address mapping
