import socket
import threading
import sys

reload(sys)

sys.setdefaultencoding("utf-8")

#port number for some reason had to be greater than 1024
port = 2009

#this is how the socket is instanced
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#make this tuple so that it can be the argument in bind() function of socket module
server_address = ('', port)

#make the socket bind to the address
serverSocket.bind(server_address)

#listen for connections made to the socket
serverSocket.listen(7)

#function to handle the requests made to the server by the client
def request(c_socket, c_address):
	
	#max size of the receiving message
	message = c_socket.recv(8192)

	#print(message)
	
	#attempt to see if the request is good
	#if so, send the OK message
	#also send the output data
	#then close the socket	
	try:
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		f.close()
		c_socket.send('HTTP/1.0 200 OK\r\n')
		c_socket.send(outputdata)
		c_socket.close()
	
	#if there is an error, send the 404 error message
	#then close the socket
	except IOError:	
		print ('error')
		c_socket.send('HTTP/1.1 404 Not Found \r\n')
		c_socket.close()

while True:
	print 'Ready to serve...'

	#get the info from the socket that is declared and defined earlier
	#create a thread where each thread runs the request function
	#daemon threads makes sure that the only time the thread exits is when the program exits
	connection, client_address = serverSocket.accept()
	request_thread = threading.Thread(target= request, args=(connection, client_address))
	request_thread.daemon = True
	request_thread.start()

