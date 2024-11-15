# MySQL Privileges Script

## Description
This script lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (localhost). The script outputs the `GRANT` statements for each user to show what privileges they have been granted.

## SQL Script
The script queries the privileges for the specified users using the `SHOW GRANTS` command.

```sql
-- Script that lists all privileges of the MySQL users
-- Query to list all privileges (GRANT) of the MySQL users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
