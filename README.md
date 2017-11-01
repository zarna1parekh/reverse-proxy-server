File description:

- code.py - The python code for reverse-proxy server
- dockerfile-mysql - Dockerfile to build the MYSQL DB image with info database and stats table
- dockerfile-python - Dockerfile to build Python Application image by running code.py
- docker-compose.yml - Dockore compose file for container configuration
- init-db.sql - MYSQL DB Configs on starting
- mysql_env - MYSQL DB enviornment variables
- requirements.txt - Packages to be installed in the Python Application Image
- run.sh - To build and start all the containers. Currently, scales python_app to 5 instances. Value can be modified in run.sh.
- test.sh - Sample test script against run.sh

Assumptions regarding packages: (assuming Linux Ubuntu Distribution)

- Docker package installed (apt-get install docker)
- Docker-compose package installed ofr version '2' (apt-get install docker-compose)
- Dependencies to run mysql client using python (apt-get install python-dev libmysqlclient-dev)

The mysql container runs on port 3306 on the container and is mapped to port 6000 on the host. The data directory is mapped to /storage/docker/mysql-datadir

Caching is provided by using a redis server. It listens on port 6379 on the host.

The python_code uses python package Flask which listens on port 5000 on the host and containe. It has the following arguments:
  -c , --cache_timer    : Cache Expiry Timer in seconds (Default: 60s)
  -p , --mysql_password : MYSQL password (Default: mypassword)
  -u , --mysql_user     : MYSQL user (Default: root)
Above values can be modified in dockerfile-python.

Make sure you are the root user and run.sh and test.sh have executable permissions

To create the dockers: ./run.sh

To test the created dockers: ./test.sh
test.sh contains a number of curl commands to query the data and statistics

A new endpoint created for statistics is /stats with "?responseTime><time in sec>" as an optional parameter.
Ex: /stats?responseTime>0.7 will return request which took longer than 0.7 seconds.


