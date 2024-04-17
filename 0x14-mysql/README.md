0x14. MySQL

https://docs.google.com/document/d/1btVRofXP75Cj90_xq2x8AmzuMPOKq6D_Dt_SCDD6GrU/edit


CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;


sudo mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"

projectcorrection280hbtn


CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));
INSERT INTO nexus6 (name) VALUES ('Leon');


GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';


sudo mysql -uholberton_user -p -e "USE tyrell_corp; SELECT * FROM nexus6;"


CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;


sudo mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'

ufw allow from 54.146.94.67 to any port 3306


cat /etc/mysql/mysql.conf.d/mysqld.cnf

sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

server-id = 1
log-bin = /var/log/mysql/mysql-bin.log
binlog_do_db = tyrell_corp

sudo service mysql restart



SHOW MASTER STATUS;

mysql> SHOW MASTER STATUS;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      154 | tyrell_corp  |                  |                   |
+------------------+----------+--------------+------------------+-------------------+


sudo mysqldump -u root -p tyrell_corp > tyrell_corp.sql

scp tyrell_corp.sql ubuntu@web-02.inm-749.tech:/tmp/

CREATE DATABASE IF NOT EXISTS tyrell_corp;

sudo mysql -u root -p tyrell_corp < /tmp/tyrell_corp.sql

sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

server-id = 2
log-bin = /var/log/mysql/mysql-bin.log
binlog_do_db = tyrell_corp
relay-log = /var/log/mysql/mysql-relay-bin.log

bind-address    = 0.0.0.0

sudo service mysql restart


CHANGE MASTER TO
  MASTER_HOST = '35.153.193.23',
  MASTER_USER = 'replica_user',
  MASTER_PASSWORD = 'replica',
  MASTER_LOG_FILE = 'mysql-bin.000001',
  MASTER_LOG_POS = 154;

START SLAVE;
SHOW SLAVE STATUS\G;


scp ubuntu@web-01.inm-749.tech:/etc/mysql/mysql.conf.d/mysqld.cnf 4-mysql_configuration_primary

scp ubuntu@web-02.inm-749.tech:/etc/mysql/mysql.conf.d/mysqld.cnf 4-mysql_configuration_replica


scp 5-mysql_backup ubuntu@web-01.inm-749.tech:~/
