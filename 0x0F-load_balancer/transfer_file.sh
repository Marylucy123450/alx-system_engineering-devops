#!/usr/bin/env bash
# Write a Bash script that transfers a file from our client to a server:

username=ubuntu
server_ip=$2
ssh_key=~/.ssh/alxse
file_path=$1
scp -i "$ssh_key" -o StrictHostKeyChecking=no "$file_path" "$username@$server_ip":~/
