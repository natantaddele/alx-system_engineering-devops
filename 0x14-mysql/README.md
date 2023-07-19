Setting Up MySQL and Creating Users for Web-01 and Web-02
This README file contains instructions on how to install MySQL 5.7.x, create a MySQL user named "holberton_user" on both Web-01 and Web-02, and grant the necessary permissions to check the replication status.

Prerequisites
Before proceeding with the installation and user creation, make sure you have:

Access to both Web-01 and Web-02 servers.
Appropriate privileges to install packages and create users (e.g., root or sudo access).
Step 1: Installing MySQL 5.7.x
Update package lists and repositories:

bash
Copy code
sudo apt update
Install MySQL Server 5.7:

bash
Copy code
sudo apt install -y mysql-server
Start the MySQL service:

bash
Copy code
sudo service mysql start
Verify the installed version:

bash
Copy code
mysql --version
The output should show the MySQL version 5.7.x.

Step 2: Creating "holberton_user" and Granting Permissions
Log in to MySQL as the root user:

bash
Copy code
sudo mysql -u root -p
Create the user "holberton_user" with the specified password and localhost as the host:

sql
Copy code
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
Grant permissions to "holberton_user" for checking the replication status:

sql
Copy code
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
Flush privileges for the changes to take effect:

sql
Copy code
FLUSH PRIVILEGES;
Exit MySQL:

sql
Copy code
quit
Step 3: SSH Configuration
Make sure that task #3 of your SSH project is completed for both Web-01 and Web-02. Ensure that the necessary public keys are added to both servers for secure access.

Verification
To verify that the "holberton_user" has been created with the correct permissions, log in to each server and run the following command:

bash
Copy code
mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter the password for "holberton_user" when prompted. The output should show the granted permissions.
