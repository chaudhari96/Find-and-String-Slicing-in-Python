#create a socket and server and then send and retrieve data to and from the server
import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('coursera.org', 80))
cmd='GET https://www.coursera.org HTTPS/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    d=mysock.recv(512)
    if (len(d)<1):
        break
    print(d.decode())
mysock.close()
