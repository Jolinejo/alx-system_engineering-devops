# Fix the apache error
exec{'fix error line':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path     => '/bin/:/usr/local/bin/'
}
