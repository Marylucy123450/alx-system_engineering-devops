#!/usr/bin/env bash

# Update package list and install snapd
sudo apt -y update
sudo apt -y install snapd

# Install Certbot via snap
sudo apt-get -y remove certbot
sudo apt-get -y install certbot

# Stop HAProxy service temporarily
sudo service haproxy stop

# Define domain
DOMAIN='www.inm-749.tech'

# Obtain SSL certificate using Certbot standalone mode
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d "$DOMAIN"

# Define certificate folder
CERT_FOLDER="/etc/letsencrypt/live/$DOMAIN"

# List contents of the Let's Encrypt certificate directory
sudo ls "$CERT_FOLDER"

# Concatenate fullchain.pem and privkey.pem into a single certificate file
sudo bash -c "cat '$CERT_FOLDER/fullchain.pem' '$CERT_FOLDER/privkey.pem' > '$CERT_FOLDER/$DOMAIN.pem'"


# Configure HAProxy
sudo tee /etc/haproxy/haproxy.cfg > /dev/null <<EOF
global
        log /dev/log    local0
        log /dev/log    local1 notice
        chroot /var/lib/haproxy
        stats socket /run/haproxy/admin.sock mode 660 level admin
        stats timeout 30s
        user haproxy
        group haproxy
        daemon

        # Default SSL material locations
        ca-base /etc/ssl/certs
        crt-base /etc/ssl/private

        # See: https://ssl-config.mozilla.org/#server=haproxy&server-version=2.0.3&config=intermediate
        ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
        ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
        ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets

defaults
        log     global
        mode    http
        option  httplog
        option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
        errorfile 400 /etc/haproxy/errors/400.http
        errorfile 403 /etc/haproxy/errors/403.http
        errorfile 408 /etc/haproxy/errors/408.http
        errorfile 500 /etc/haproxy/errors/500.http
        errorfile 502 /etc/haproxy/errors/502.http
        errorfile 503 /etc/haproxy/errors/503.http
        errorfile 504 /etc/haproxy/errors/504.http

frontend www-http
        bind *:80
        http-request add-header X-Forwarded-Proto http
        default_backend web-backend
        redirect scheme https code 301 if !{ ssl_fc }

frontend www-https
        bind *:443 ssl crt /etc/letsencrypt/live/www.inm-749.tech/www.inm-749.tech.pem
        http-request add-header X-Forwarded-Proto https
        default_backend web-backend

backend web-backend
        balance roundrobin
        server 339243-web-01 35.153.193.23:80 check
        server 339243-web-02 54.146.94.67:80 check

EOF

# Start HAProxy service
sudo service haproxy start

# Verify HAProxy configuration
curl -sI 127.0.0.1

sudo service haproxy status
