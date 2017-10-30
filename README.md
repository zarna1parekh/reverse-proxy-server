Assumptions regarding packages:

- Docker package installed
- Dependencies to run mysql client using python (python-dev, libmysqlclient-dev)

The mysql container runs on port 3306 on the container and is mapped to port 6000 on the host. The data directory will be mapped to /storage/docker/mysql-datadir

The python_code uses the python package Flask which listens on port 5000 on the host and container

Make sure you are the root user and run.sh and test.sh have executable permissions

To create the dockers: ./run.sh

To test the created dockers: ./test.sh

