#ADAPTIVE LABS TEST
===


## SETUP
===

### MYSQL database
===

You can execute these lines in your mysql commandline to setup a database.
```sql
CREATE DATABASE adaptivetest DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'adaptivetest'@'localhost' IDENTIFIED BY 'adaptivetest;
GRANT ALL ON adaptivetest.* TO 'adaptivetest'@'localhost';
FLUSH PRIVILEGES;
```
