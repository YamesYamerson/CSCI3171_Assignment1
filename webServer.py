#import socket module
import socket
import sys # In order to terminate the program
import threading

#############################################
###       A Basic Socket Web Server       ###
#############################################
#Constants
HEADER = 1024
PORT = 5050 #Port to listen to
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

#Prepare a sever socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Standard loopback interface address
serverSocket.bind(ADDR) #binds socket to address



def handle_client(connectionSocket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            message = connectionSocket.recv(1024)
            print(f"[MESSAGE] {message}\n [SPLIT MESSAGE] {message.split()[0]}")
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            print(f"[OUTPUT DATA] {outputdata}")

            #Send HTTP header line into socket
            connectionSocket.send(outputdata)
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()

                if message == DISCONNECT_MESSAGE:
                    connectionSocket.close()

            connectionSocket.send("Message Received".encode(FORMAT))
            sys.exit()  # Terminate the program after sending the corresponding data

        except IOError:
            connectionSocket.send("[404] File Not Found")
            connectionSocket.close()           #Fill in start

            sys.exit()  # Terminate the program after sending the corresponding data


def start():
    serverSocket.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = serverSocket.accept() #waits for new connection from server
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")

start()
handle_client()


#REFS#
#Python Socket Programming Tutorial -Tech With Tim
#https://zetcode.com/python/socket/
#https://www.pluralsight.com/guides/web-scraping-with-request-python



