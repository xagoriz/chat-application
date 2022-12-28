#!/usr/bin/python
import threading 
import socket

host = '127.0.0.1' #localhost or the ip address of the server
port = '99872' # do not use well known ports

server = socket.socket(socket.AF_INET, socket.SOCKS_STREAM)

server.bind = ((host, port))
server.listen()

# defining methods
#2 empty lists, the clients and the nicknames
# can use csv or a database like mongoDB
clients = []
nicknames = []

#broadcast funtion

def broadcast(message):
    for client in clients:
        clinet.send(message)

#handeling
def handle(client):
    while(true):
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('f{nickname} has left the chat'.encode('ascii1'))
            nicknames.remove(nickname)
            break


