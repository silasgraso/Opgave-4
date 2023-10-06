from socket import *

serverName = "localhost"
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    command = input('Enter command (Random/Add/Subtract) or "quit" to exit: ')
    
    if command == "quit":
        clientSocket.send(command.encode())
        break
    
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    
    sentence = command + ";" + num1 + ";" + num2 + "\n"
    clientSocket.send(sentence.encode())
    
    response = clientSocket.recv(1024)
    print('Server response: ', response.decode())

clientSocket.close()
