#! /usr/bin/env python3



import socket
import os
from Crypto.Cipher import AES
from Crypto import Random

# key must be sixteen byte
key = b'secretkey0123456'

# generate the initialization vector using the Random function
iv = Random.new().read(AES.block_size)
# create new chiper object with For `MODE_CFB`, *plaintext* length (in bytes) must be a multiple
#of 8.
chipher = AES.new(key, AES.MODE_CFB, iv)

def decrypt(message):
    #decrypt message using chiper object built in function
    return  chipher.decrypt(message)


def connect():
    #create low-level socket object using standard settings
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect to server by providing IP and Port number ( in this case )
    ip = "127.0.0.1"
    port = 8080

    sock.connect((ip, port))

    while True:
        # receive byte in 1 Gig chuncks
        commandLine = sock.recv(1024)
        # receive byte in 1 Gig chuncks and decrypt
        decryptedCommandLine =  decrypt(sock.recv(1024))

        # terminate socket if user types terminate
        if b'terminate' in commandLine:
            sock.close()
            break
        else:
            #print
            print("\n\n\n")
            print(b'Before decription:' + commandLine)
            print("\n\n\n")
            print(b'After decription: ' + decryptedCommandLine)
            print("\n\n\n")






#start with connect function
if __name__=="__main__":
    connect()




































#end
