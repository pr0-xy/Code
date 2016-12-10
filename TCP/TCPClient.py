import socket

target_host = "127.0.0.1"
target_port = 9999

# Create socket object
# AF_INET indicates to use IPV4 and SOCK_STREAM indicates it will use TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the server
client.connect((target_host,target_port))

# Send data to the server 
client.send("I am connected")

# Receive data from the server
response = client.recv(4096)

print response
