from socket import *
serverName = 'DESKTOP-G72GRFD'
#Hostname of desktop which I'm using as server
serverPort = 12000

clientSocket = socket(AF_INET,
                      SOCK_DGRAM)
clientSocket.settimeout(10) #Timeout after 10 seconds

try:
    message = input('Input lowercase sentence')
    clientSocket.sendto(message.encode(),
                        (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())

except timeout:
    print("Connection timed out")

finally:
    clientSocket.close()
