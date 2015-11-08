import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 4560

# Binds the server to address and port.
s.bind((host, port))

# Listens for a max of 5 clients.
s.listen(5)
while True:

	# Accepts a connection.
	c, addr = s.accept()
	print('Recieved connection from', addr)

	# Receives data from the client.
	data = c.recv(4096).decode('utf8')

	# Responds with a 'PONG'.
	if data == 'PING':
		print('<', data)
		c.send(bytes('PONG', 'utf8'))
		print('>', 'PONG')

	# Closes the connection.
	c.close()