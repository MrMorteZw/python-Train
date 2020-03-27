import socket

 
#ip local baray port
localIP     = "127.0.0.1"
#port ke eshghal mikone
localPort   = 20001
#100 bit
bufferSize  = 1024

 
#msg ke az sv miad
msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# sabt sv udp

UDPServerSocket.bind((localIP, localPort))

#print mikone agar code dorost bashe 

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):
    #1000bit etelaat az soketi ke sakhte migire mirize be sorat arrayhe ke avalish payame dovoi ferestande
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    #index 0 k array aval bashe hast
    message = bytesAddressPair[0]
    #index 1 ke array dovom bashe hast
    address = bytesAddressPair[1]

    # etlaat mirize to moteghayer
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    #chap mikone
    print(clientMsg)
    print(clientIP)

   

    #payam bar migardone be client

    UDPServerSocket.sendto(bytesToSend, address)