0x13. Firewall

# To configure firewall to redirect port 8080/TCP to port 80/TCP
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
