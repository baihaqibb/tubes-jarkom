from socket import *
import sys

if len(sys.argv) != 4:
    print("Syntax Error")
    sys.exit(1)

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))
if filename[0] != "/":
    filename = "/" + filename
request = f"GET {filename} HTTP/1.1\r\nHost: {serverHost}\r\nConnection: close\r\n\r\n"
clientSocket.send(request.encode("UTF-8"))
response = b""
while True:
    part = clientSocket.recv(1024)
    if not part:
        break
    response += part
clientSocket.close()
print(response.decode("UTF-8"))

