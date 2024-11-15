# MySQL User Privileges

This script is used to list the privileges of MySQL users.

## SQL Script:

-- Script that lists all privileges of the MySQL users  
-- Query to list all privileges (GRANT) of the MySQL users  
SHOW GRANTS FOR 'user_0d_1'@'localhost';  
SHOW GRANTS FOR 'user_0d_2'@'localhost';  

## Expected Outputs:

1. **If the users don't exist**:  
   Correct output:  

