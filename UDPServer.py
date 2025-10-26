from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The servers ready to receive')
def check(sentence):
    try:
        sentenceInt = int(sentence) 
        #Converts server input to int
        valuex = sentenceInt % 2
        #Modulo to check if even or odd
        if valuex == 1:
            answer = "Odd"
            
        else:
            answer = "Even"
    except ValueError:
        answer = "Please input a whole number"
        #Error catching if input isn't an integer like fractions aka floats
    except TypeError:
        answer = "Please input a whole number"
        #Error catching for wrong data type
    
    return answer
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = check(message.decode())
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

