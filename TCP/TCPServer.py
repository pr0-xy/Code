import socket
import threading 

bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP and Port we want the server to listen on 
server.bind((bind_ip,bind_port))

# Tell the server where to start listening, maximum amount of backlog connections = 5	
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# Client Handling thread
def handle_client(client_socket):

	# Print what the client sends
	request = client_socket.recv(1024)

	print "[*] Received: %s" % request

	# Send back a packet
	client_socket.send("ACK!")
	
	client_socket.close()

while True:
	
	client,addr = server.accept()

	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
	
	# Allow client thread to handle incoming data 
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()

		
        








