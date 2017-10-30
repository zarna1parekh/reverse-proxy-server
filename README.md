File description:

code.py - The python code for reverse-proxy server
dockerfile-mysql - Dockerfile to build the MYSQL DB image with info database and stats table
dockerfile-python - Dockerfile to build Python Application image by running code.py
init-db.sql - MYSQL DB Configs on starting
mysql_env - MYSQL DB enviornment variables
requirements.txt - Packages to be installed in the Python Application Image
run.sh - To buil and start all the containers
test.sh - Sample test script against run

Assumptions regarding packages:

- Docker package installed
- Dependencies to run mysql client using python (python-dev, libmysqlclient-dev)

The mysql container runs on port 3306 on the container and is mapped to port 6000 on the host. The data directory will be mapped to /storage/docker/mysql-datadir

The python_code uses the python package Flask which listens on port 5000 on the host and container

Make sure you are the root user and run.sh and test.sh have executable permissions

To create the dockers: ./run.sh

To test the created dockers: ./test.sh

