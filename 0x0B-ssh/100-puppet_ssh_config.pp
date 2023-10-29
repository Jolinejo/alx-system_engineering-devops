#configure ssh
# Create file
file_line { 'line2':
  path => '~/.ssh/config',
  line => 'PasswordAuthentication no',
}
file_line { 'line3':
  path => '~/.ssh/config',
  line => 'IdentityFile ~/.ssh/school',
}
