from socket import *
from struct import *
import threading

def decode(encoded):
    i = 0
    letter = encoded[0]
    decoded = ''

    while i < len(encoded):
        asciiNum = ord(letter)              # Retorna o valor ascii do caracter
        if asciiNum - 3 < 97:               # Se menor que a(97) voltamos ao fim z(122)
            remnant = 97 - (asciiNum - 3)
            asciiNum = 123 - remnant
        else:
            asciiNum = asciiNum - 3         # Subtrai o valor ascii na letra
        decoded += chr(asciiNum)            # Retorna o caracter correspondente a letra codificada
        i += 1
        if i < len(encoded):                 # Se chegar ao fim da string o mesage[i] não existe
            letter = encoded[i]
    return decoded

def thread(connectionSocket):
    # size = connectionSocket.recv(1024)
    # size = unpack('>I', size)
    message = connectionSocket.recv(1024).decode()
    # X = connectionSocket.recv(1024)
    # X = unpack('>I', X)
    decoded = decode(message)
    connectionSocket.send(decoded.encode())
    print(f'Sended to client: {decoded}')
    connectionSocket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    port = int(input('Insert the port: '))
    serverSocket.bind(('127.0.0.1', port))
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        connectionSocket, addr = serverSocket.accept()                      # Aceita a conexão
        threading.Thread(target=thread, args=(connectionSocket,)).start()   # Abre uma thread para o cliente

if __name__ == '__main__':
    main()