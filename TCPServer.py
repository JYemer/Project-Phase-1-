from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen()
print('The server is ready to receive')
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
        #Error catching
    except TypeError:
        answer = "Please input a whole number"
        #Error catching
    
    return answer
while True:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    isEvenOrOdd = check(sentence)
    connectionSocket.send(isEvenOrOdd.encode())
    connectionSocket.close()
    #References

