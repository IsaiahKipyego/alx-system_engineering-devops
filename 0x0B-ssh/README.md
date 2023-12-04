0x0B. SSH
0-use_a_private_key
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

1-create_ssh_key_pair
Write a Bash script that creates an RSA key pair.

2-ssh_config
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

0x0B-ssh

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
100-puppet_ssh_config.pp

Requirements:

Your SSH client configuration must be configured to use the private key ~/.ssh/school Your SSH client configuration must be configured to refuse to authenticate using a password
