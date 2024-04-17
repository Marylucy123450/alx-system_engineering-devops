# Using strace, find out why Apache is returning a 500 error. Once you find
# the issue, fix it and then automate it using Puppet

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

