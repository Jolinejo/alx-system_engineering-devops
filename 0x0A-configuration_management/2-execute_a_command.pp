#kill a process
exec {'kill_process':
    command  => 'pkill -f killmenow',
    path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    provider => 'shell',
}
