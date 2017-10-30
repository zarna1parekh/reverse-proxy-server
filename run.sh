!#/bin/bash

#Create docker network
sudo docker network create thousand_eyes

#create mysql_image image
sudo docker build -t mysql_image -f dockerfile-mysql .

#create a volume directory on the host
sudo mkdir -p /storage/docker/mysql-datadir

#run the mysql DB docker
#sudo docker run --name "mysql_db" -e MYSQL_ROOT_PASSWORD=mypassword  -p 6000:3306 --network "thousand_eyes" -d "mysql_image"
sudo docker run --name "mysql_db" --env-file ./mysql_env -p 6000:3306 --network "thousand_eyes" --volume=/storage/docker/mysql-datadir:/var/lib/mysql -d mysql_image 

#create python_app image
sudo docker build -t python_app_image .

#run the python application docker
sudo docker run --name python_code -p 5000:5000 --network "thousand_eyes" -d python_app_image