#configure ssh
# Create file
file_line { 'line':
  path => '~/.ssh/config',
  line => 'Host 54.236.47.113',
}
file_line { 'line2':
  path => '~/.ssh/config',
  line => 'PasswordAuthentication no',
}
file_line { 'line3':
  path => '~/.ssh/config',
  line => 'IdentityFile ~/.ssh/school',
}
