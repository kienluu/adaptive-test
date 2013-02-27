#ADAPTIVE LABS TEST
===

See specifications [here](https://github.com/kienluu/adaptive-test/blob/master/Specifications.md)

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

To begin a new database, run the django syncdb and south migrate commands
```bash
$ ./manage.py syncdb
$ ./manage.py migrate
```

### Others

TODO: Create documentation for another user to setup this project
