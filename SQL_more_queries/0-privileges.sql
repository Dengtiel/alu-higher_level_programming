-- Create the users (if not already created)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Grant privileges to user_0d_2
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Show the privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show the privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
