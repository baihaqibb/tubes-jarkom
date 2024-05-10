from socket import *

print("Starting server...")
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 42069
serverAddress = gethostbyname(gethostname())
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen(1)
print(f"Server is up and running!, Listening on {serverAddress} at port {serverPort}")
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Established connection with {addr}")
    try:
        msg = connectionSocket.recv(1024)
        filename = msg.split()[1]
        file = open(filename[1:])
        data = file.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode("UTF-8"))
        for i in range(0, len(data)):
            connectionSocket.send(data[i].encode("UTF-8"))
        connectionSocket.send("\r\n".encode("UTF-8"))
        print(f"Ended connection with {addr}")
        connectionSocket.close()
    except:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode("UTF-8"))
        print(f"Ended connection with {addr}")
        connectionSocket.close()
serverSocket.close()