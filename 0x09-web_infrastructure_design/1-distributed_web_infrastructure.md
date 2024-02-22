![](https://github.com/Isaac-Ndirangu-Muturi-749/alx-system_engineering-devops/blob/main/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png)


**Three-Server Web Infrastructure Design**

**Overview:**
- The web infrastructure is designed for hosting the website www.foobar.com.
- This infrastructure includes three servers, a load balancer, and a MySQL database.

**Components:**

1. **Server 1 (Primary Application Server):**
   - Hosts the primary instance of the application server.
   - Executes dynamic code, processes requests, and communicates with the database.
   - This server actively serves user requests.

2. **Server 2 (Replica Application Server):**
   - Hosts a replica instance of the application server.
   - Provides redundancy and load balancing capabilities.
   - Takes over if the primary server experiences issues or during high traffic.

3. **Web Server (Nginx):**
   - Handles HTTP requests, manages connections, and serves static content.
   - Acts as a reverse proxy, forwarding dynamic requests to the application servers.
   - Facilitates efficient load balancing.

4. **Load Balancer (HAProxy):**
   - Distributes incoming traffic across the two application servers.
   - Configuration: Round-robin algorithm for load distribution.
   - Active-Active Setup: Both application servers actively handle user requests simultaneously.

5. **Application Files (Code Base):**
   - Contains the source code of the website/application.
   - Executed by both the primary and replica application servers.

6. **Database (MySQL - Primary-Replica Cluster):**
   - Primary Node: Accepts both read and write operations.
   - Replica Node: Replicates data from the primary node and handles read operations.
   - Enhances data availability, fault tolerance, and load distribution.

**Roles:**

- **Server 1 (Primary Application Server):**
  - Serves as the primary instance of the application server.
  - Handles user requests actively.

- **Server 2 (Replica Application Server):**
  - Acts as a replica instance of the application server.
  - Provides redundancy and load balancing capabilities.

- **Web Server (Nginx):**
  - Manages HTTP requests, connections, and serves static content.
  - Acts as a reverse proxy, directing dynamic requests to application servers.

- **Load Balancer (HAProxy):**
  - Distributes incoming traffic among application servers using a round-robin algorithm.
  - Enables an Active-Active setup, improving system performance.

- **Application Files (Code Base):**
  - Contains the source code executed by both application servers.

- **Database (MySQL - Primary-Replica Cluster):**
  - Primary Node: Accepts both read and write operations.
  - Replica Node: Replicates data and handles read operations.
  - Enhances data availability and fault tolerance.

**Issues:**

1. **Single Point of Failure (SPOF):**
   - The load balancer is a potential SPOF; its failure would disrupt traffic distribution.

2. **Security Issues:**
   - Lack of firewall protection may expose servers and the database to security threats.
   - The absence of HTTPS may compromise the security of data in transit.

3. **No Monitoring:**
   - No monitoring system in place for tracking server health, performance, and potential issues.