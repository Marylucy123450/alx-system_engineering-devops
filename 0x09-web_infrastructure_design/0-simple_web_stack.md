![](https://github.com/Isaac-Ndirangu-Muturi-749/alx-system_engineering-devops/blob/main/0x09-web_infrastructure_design/0-simple_web_stack.png)



**Web Infrastructure Design**

**Overview:**
- The web infrastructure is designed for hosting the website reachable via www.foobar.com.
- The infrastructure includes a single server with a LAMP stack.

**Components:**
1. **Server:**
   - Physical or virtual machine responsible for hosting the entire infrastructure.
   - IP Address: 8.8.8.8

2. **Domain Name:**
   - www.foobar.com
   - A human-readable address pointing to the server's IP (8.8.8.8).
   - Facilitates user-friendly access to the website.

3. **DNS Record for www:**
   - www is a subdomain of foobar.com.
   - It is a CNAME (Canonical Name) record pointing to the domain (foobar.com).
   - Resolves to the server's IP address (8.8.8.8).

4. **Web Server (Nginx):**
   - Receives and processes HTTP requests from users.
   - Serves static content, manages connections, and acts as a reverse proxy.
   - Listens for requests on port 80.

5. **Application Server:**
   - Executes dynamic code, processes requests, and communicates with the database.
   - Responsible for running the application logic.
   - Communicates with the web server using a defined protocol (e.g., FastCGI).

6. **Application Files (Code Base):**
   - Contains the source code of the website/application.
   - Executed by the application server to generate dynamic content.

7. **Database (MySQL):**
   - Stores and manages the website's data.
   - Application server communicates with the database to retrieve or store information.

**Roles:**
- **Server:**
  - Hosts and manages the entire web infrastructure.

- **Domain Name:**
  - Provides a human-readable address for accessing the website.

- **DNS Record for www:**
  - Resolves the www subdomain to the server's IP.

- **Web Server (Nginx):**
  - Handles HTTP requests, manages connections, and serves static content.
  - Acts as a reverse proxy, forwarding dynamic requests to the application server.

- **Application Server:**
  - Executes dynamic code, processes requests, and communicates with the database.
  - Responsible for running the application logic.

- **Application Files (Code Base):**
  - Contains the source code of the website/application.
  - Executed by the application server.

- **Database (MySQL):**
  - Stores and manages the website's data.
  - Application server communicates with the database.

**Issues:**
1. **Single Point of Failure (SPOF):**
   - The entire infrastructure relies on a single server.
   - If the server fails, the entire website becomes inaccessible.

2. **Downtime during Maintenance:**
   - Deploying new code or restarting the web server requires downtime.
   - Users may experience disruptions during maintenance.

3. **Limited Scalability:**
   - Difficult to handle a large influx of traffic.
   - Scaling options (e.g., load balancing) are limited in a single-server setup.