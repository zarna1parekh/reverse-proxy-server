create database info;
use info;
create table stats (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, timeStamp VARCHAR(255), url VARCHAR(1000), responseTime FLOAT);
