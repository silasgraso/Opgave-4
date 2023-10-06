from socket import *
import threading

def clientHandler(connectionSocket, addr):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if not sentence:
            break

        command, num1, num2 = sentence.split(";")

        if command == "Random":
            num1 = int(num1)
            num2 = int(num2)
            import random
            response = str(random.randint(num1, num2))
            connectionSocket.send(response.encode())
        elif command == "Add":
            num1 = int(num1)
            num2 = int(num2)
            response = str(num1 + num2)
            connectionSocket.send(response.encode())
        elif command == "Subtract":
            num1 = int(num1)
            num2 = int(num2)
            response = str(num1 - num2)
            connectionSocket.send(response.encode())
        else:
            connectionSocket.send("Invalid command".encode())

    print("Connection closed by client")
    connectionSocket.close()

serverPort = 13000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listens')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=clientHandler, args=(connectionSocket, addr)).start()
