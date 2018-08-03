import socket

port = 2009
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('', port)

#connect to the server
client_socket.connect(server_address)

#send the GET function with the path of the HTML file
client_socket.send("GET /hello_world.html")

while True:
	message = client_socket.recv(8192)
	print(message)
	exit()
