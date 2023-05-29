# Web Infrastructure README

This README file provides an overview of the web infrastructures designed to host the website www.foobar.com. It includes information about the infrastructure components, their roles, configuration specifics, and potential issues.

## Infrastructure 1: Single-Server Web Infrastructure

### Components:
- 1 Server: Physical or virtual machine hosting the website.
- Web Server (Nginx): Receives and serves incoming HTTP requests.
- Application Server: Executes the website's application code.
- Application Files: Contains the codebase of the website's application logic.
- Database (MySQL): Stores and manages the website's data.
- Domain Name: foobar.com configured with a www record pointing to the server IP.

### Specifics:
- A server hosts the website, while Nginx serves incoming requests.
- The application server executes the website's application code.
- MySQL database stores and manages website data.
- The website is accessible via www.foobar.com.
- HTTP protocol is used for communication between the server and user's computer.

### Issues:
- Single Point of Failure (SPOF): If the server fails, the website becomes inaccessible.
- Downtime during Maintenance: Deploying new code or performing maintenance requires restarting the web server, resulting in temporary downtime.
- Limited Scalability: With only one server, handling high incoming traffic may be challenging.

## Infrastructure 2: Three-Server Web Infrastructure with Load Balancer

### Components:
- 2 Servers: Provides redundancy and handles increased traffic.
- Load Balancer (HAProxy): Distributes incoming requests among servers.
- Web Server (Nginx): Receives and serves incoming HTTP requests.
- Application Server: Executes the website's application code.
- Application Files: Contains the codebase of the website's application logic.
- Database (MySQL): Stores and manages the website's data.
- Domain Name: foobar.com configured with a www record pointing to the load balancer IP.

### Specifics:
- Two servers provide redundancy and improved performance.
- HAProxy load balancer distributes incoming requests using a round-robin algorithm.
- Nginx web server serves web pages, while the application server executes application code.
- MySQL database stores and manages website data.
- The website is accessible via www.foobar.com, which points to the load balancer.

### Issues:
- Single Point of Failure (SPOF): The load balancer can be a potential SPOF.
- Security Issues: Lack of firewall and HTTPS exposes the infrastructure to potential threats.
- No Monitoring: Absence of monitoring tools makes it challenging to track the infrastructure's performance and health.

## Infrastructure 3: Three-Server Web Infrastructure with Load Balancer and Primary-Replica Database Cluster

### Components:
- 2 Servers: Provides redundancy and handles increased traffic.
- Load Balancer (HAProxy): Distributes incoming requests among servers.
- Web Server (Nginx): Receives and serves incoming HTTP requests.
- Application Server: Executes the website's application code.
- Application Files: Contains the codebase of the website's application logic.
- Database (MySQL): Primary-Replica cluster for storing and managing website data.
- Domain Name: foobar.com configured with a www record pointing to the load balancer IP.

### Specifics:
- Two servers provide redundancy and improved performance.
- HAProxy load balancer distributes incoming requests using a round-robin algorithm.
- Nginx web server serves web pages, while the application server executes application code.
- MySQL database configured as a Primary-Replica (Master-Slave) cluster for data replication and read scaling.
- The website is accessible via www.foobar
