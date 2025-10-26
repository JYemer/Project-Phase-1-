from socket import *
serverName = '10.0.0.87'
#IP of my desktop which I'm using as a server
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(10)

try:
    clientSocket.connect((serverName,serverPort))
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print ('From Server:', modifiedSentence.decode())
except timeout:
    print("Connection timed out")

finally:
    clientSocket.close()