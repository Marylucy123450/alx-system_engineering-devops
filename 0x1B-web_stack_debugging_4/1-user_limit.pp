# Increase hard and soft file limit for user holberton

exec { 'increase-file-limit-for-holberton-user':
  command => 'sed -i \
  "s/holberton hard nofile 5/holberton hard nofile 50000/; \
  s/holberton soft nofile 4/holberton soft nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
