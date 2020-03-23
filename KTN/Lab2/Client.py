import time
from socket import *
print("CLIENT WINDOW")

# Get the server hostname and port as command line arguments
host = '192.168.1.6' # FILL IN START		# FILL IN END
port = 12000  # FILL IN START		# FILL IN END
timeout = 1 # in seconds

# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

ptime = 0

# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description
    data = raw_input()#.lower()# FILL IN START		# FILL IN END

    try:
        # Record the "sent time"
        sendTime = time.clock()

        # Send the UDP packet with the ping message
        clientSocket.sendto(data,(host, port))

        # Receive the server response|
        dataReceived, serverAddress = clientSocket.recvfrom(2048)

        # Record the "received time"
        receiveTime = time.clock()

        # Display the server response as an output
        print(dataReceived)
        # Round trip time is the difference between sent and received time
        roundTripTime = (receiveTime - sendTime) * 1000 #in miliseconds
        #print("RTT:", roundTripTime)
        print("RTT: %.3f ms" % roundTripTime)

    except:
        # Server does not response
	    # Assume the packet is lost
        print "Request timed out."
        continue
clientsocket.close()

