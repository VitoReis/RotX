from socket import *
from struct import *
import threading
from _thread import *

def decode(encoded):
    i = 0
    index = 0
    letter = encoded[0]
    decoded = ''

    while i < len(encoded):
        asciiNum = ord(letter)              # Retorna o valor ascii do caracter
        if asciiNum - 3 < 97:               # Se menor que a(97) voltamos ao fim z(122)
            rest = 97 - (asciiNum - 3)
            asciiNum = 123 - rest
        else:
            asciiNum = asciiNum - 3         # Subtrai o valor ascii na letra
        decoded += chr(asciiNum)            # Retorna o caracter correspondente a letra codificada
        i += 1
        if i < len(encoded):                 # Se chegar ao fim da string o mesage[i] não existe
            letter = encoded[i]
    return decoded

def thread(connectionSocket):
    while True:
        print('thread start')
        message = connectionSocket.recv(1024).decode()
        print(f'From client: {message}')
        decoded = decode(message)
        print(f'Sending to client: {decoded}')
        connectionSocket.send(decoded.encode())
        print('thread end')
    connectionSocket.close()


port = int(input('Insert the port: '))
# port = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', port))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Lock()
    threading.Thread(target=thread, args=(connectionSocket,)).start()
    # size = connectionSocket.recv(1024)
    # size = unpack('>I', size)
    # print(size)
    # message = connectionSocket.recv(1024).decode()
    # print(f'From client: {message}')
    # decoded = decode(message)
    # print(f'Sending to client: {decoded}')
    # connectionSocket.send(decoded.encode())
    connectionSocket.close()