![](https://github.com/Isaac-Ndirangu-Muturi-749/alx-system_engineering-devops/blob/main/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png
)

**Three-Server Web Infrastructure Design with Security, HTTPS, and Monitoring**

**Overview:**
- The web infrastructure is designed for hosting the website www.foobar.com with enhanced security, encrypted traffic (HTTPS), and comprehensive monitoring.
- This infrastructure includes three servers, three firewalls, SSL certificate for HTTPS, and monitoring clients for data collection.

**Components:**

1. **Server 1 (Primary Application Server):**
   - Hosts the primary instance of the application server.
   - Executes dynamic code, processes requests, and communicates with the database.
   - This server actively serves user requests.

2. **Server 2 (Replica Application Server):**
   - Hosts a replica instance of the application server.
   - Provides redundancy and load balancing capabilities.
   - Takes over if the primary server experiences issues or during high traffic.

3. **Server 3 (Monitoring Server):**
   - Dedicated server for monitoring purposes.
   - Collects and processes monitoring data from other servers.

4. **Firewall 1, Firewall 2, and Firewall 3:**
   - Implement network security policies to control and monitor incoming and outgoing traffic.
   - Safeguard servers from unauthorized access and potential cyber threats.

5. **Web Server (Nginx):**
   - Handles HTTP requests, manages connections, and serves static content.
   - Acts as a reverse proxy, forwarding dynamic requests to the application servers.
   - Supports SSL termination to enable HTTPS.

6. **Load Balancer (HAProxy):**
   - Distributes incoming traffic among the two application servers.
   - Terminate SSL connections for enhanced security.

7. **Application Files (Code Base):**
   - Contains the source code of the website/application.
   - Executed by both the primary and replica application servers.

8. **Database (MySQL - Primary-Replica Cluster):**
   - Primary Node: Accepts both read and write operations.
   - Replica Node: Replicates data from the primary node and handles read operations.
   - Enhances data availability, fault tolerance, and load distribution.

9. **SSL Certificate:**
   - Secures communication between clients and the web server using HTTPS.
   - Encrypts data in transit to protect it from interception and tampering.

10. **Monitoring Clients (Data Collectors):**
    - Deployed on each server to collect performance, health, and other relevant data.
    - Transmit data to the centralized monitoring server.

**Roles:**

- **Server 1 (Primary Application Server):**
  - Serves as the primary instance of the application server.
  - Handles user requests actively.

- **Server 2 (Replica Application Server):**
  - Acts as a replica instance of the application server.
  - Provides redundancy and load balancing capabilities.

- **Server 3 (Monitoring Server):**
  - Dedicated for collecting and processing monitoring data.

- **Firewall 1, Firewall 2, and Firewall 3:**
  - Implement network security policies.
  - Protect servers from unauthorized access.

- **Web Server (Nginx):**
  - Handles HTTP requests, manages connections, and serves static content.
  - Acts as a reverse proxy, directing dynamic requests to application servers.
  - Terminates SSL connections for HTTPS.

- **Load Balancer (HAProxy):**
  - Distributes incoming traffic among application servers.
  - Terminate SSL connections for enhanced security.

- **Application Files (Code Base):**
  - Contains the source code executed by both application servers.

- **Database (MySQL - Primary-Replica Cluster):**
  - Primary Node: Accepts both read and write operations.
  - Replica Node: Replicates data and handles read operations.
  - Enhances data availability and fault tolerance.

- **SSL Certificate:**
  - Secures communication using HTTPS.
  - Encrypts data in transit.

- **Monitoring Clients (Data Collectors):**
  - Collects and transmits data to the centralized monitoring server.

**Issues:**

1. **Terminating SSL at Load Balancer Level:**
   - SSL termination at the load balancer might expose data during internal communication between the load balancer and application servers.

2. **Single MySQL Server Capable of Accepting Writes:**
   - A single point of failure in the database system.
   - The inability to distribute write operations might result in performance bottlenecks.

3. **Uniform Components Across Servers:**
   - Lack of diversity in server components may lead to uniform vulnerabilities.
   - Affects resilience and security posture.