#import socket module
import socket
import sys # In order to terminate the program
import struct
import threading

#############################################
###       A Basic Socket Web Server       ###
#############################################
#Constants
HEADER = 64
PORT = 5050 #Port to listen to
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Standard loopback interface address
#Prepare a sever socket
serverSocket.bind(ADDR) #binds socket to address


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        message_length = conn.recv(HEADER).decode(FORMAT)
        message_length = int(message_length)
        message = conn.recv(message_length).decode(FORMAT)

        if message == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}]{message}")

        conn.close()


#handles new connections and distributes them
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

#while True:
#Establish the connection
#       print('Ready to serve...') #Waiting Message
#    connectionSocket, addr = serverSocket.accept() #Accepts connection socket

#try:
#    message = connectionSocket.recv(1024)
#    filename = message.split()[1]
#    f = open(filename[1:])
#    outputdata = #Fill in start #Fill in end
#    #Send one HTTP header line into socket
#    #Fill in start
#    #Fill in end
#    #Send the content of the requested file to the client
#
#for i in range(0, len(outputdata)):
#    connectionSocket.send(outputdata[i].encode())
#    connectionSocket.send("\r\n".encode())
#    connectionSocket.close()
#
#except IOError:
#    #Send response message for file not found
#    #Fill in start
#    #Fill in end
#    #Close client socket
#    #Fill in start
#    #Fill in end
#    serverSocket.close()
#    sys.exit()#Terminate the program after sending the corresponding data
#
#
#    #REFS#
#    #Python Socket Programming Tutorial -Tech With Tim
