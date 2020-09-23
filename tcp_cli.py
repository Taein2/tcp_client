from socket import *

HOST = "163.239.27.151"
PORT = 12134


csock = socket(AF_INET, SOCK_STREAM)
csock.connect((HOST, PORT))

print("conenct is success")

while True:
    print('-----------------------------')
    msg = raw_input('Send Message : ')
    if msg == 'q':
        break

    csock.send(msg.encode())

    res = csock.recv(20).decode()
    print('Received from the server : ' + res)
    print('-----------------------------')

csock.close()
exit()
