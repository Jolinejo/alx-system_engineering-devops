#handle many requests
exec {'fix_ulimit':
  provider => shell,
  command  => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
  path     => '/bin/:/usr/local/bin/'
}

exec {'restart_nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  path     => '/bin/:/usr/local/bin/'
}
