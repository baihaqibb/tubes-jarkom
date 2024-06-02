from socket import *
import threading

def handleClient(connectionSocket, addr):
    print(f"Established connection with {addr}")
    print(f"Active Connections: {threading.active_count()-1}")
    try:
        msg = connectionSocket.recv(1024)
        filename = msg.split()[1]
        file = open(filename[1:])
        data = file.read()
        response = "HTTP/1.1 200 OK\r\n\r\n" + data + "\r\n"
    except:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"
    finally:
        connectionSocket.send(response.encode("UTF-8"))
        print(f"Ended connection with {addr}")
        connectionSocket.close()

def serverStart():
    print("Starting server...")
    HOST = gethostbyname(gethostname()) # Mengambil alamat IP yang digunakan sekarang
    PORT = 42069 # Nomor Port dari Server
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(1)
    print(f"Server is up and running!, Listening on {HOST} at port {PORT}")
    while True:
        connectionSocket, addr = serverSocket.accept()
        handleThread = threading.Thread(target=handleClient, args=(connectionSocket, addr))
        handleThread.start()
    serverSocket.close()

if __name__ == "__main__":
    serverStart()