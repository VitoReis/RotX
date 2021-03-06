from socket import *
from struct import *
import threading
import sys

def decode(encoded, X):
    i = 0
    letter = encoded[0]
    decoded = ''

    while i < len(encoded):
        asciiNum = ord(letter)              # Retorna o valor ascii do caracter
        if asciiNum - X < 97:               # Se menor que a(97) voltamos ao fim z(122)
            remnant = 97 - (asciiNum - X)
            asciiNum = 123 - remnant
        else:
            asciiNum = asciiNum - X         # Subtrai o valor ascii na letra
        decoded += chr(asciiNum)            # Retorna o caracter correspondente a letra codificada
        i += 1
        if i < len(encoded):                 # Se chegar ao fim da string o mesage[i] não existe
            letter = encoded[i]
    return decoded

def thread(connectionSocket):
    connectionSocket.settimeout(15)
    try:
        X = connectionSocket.recv(4)  # Recebe um inteiro
        X = unpack('>I', X)[0]  # Atribui o primeiro valor da tupla a X
        size = connectionSocket.recv(4)  # Recebe outro inteiro
        size = unpack('>I', size)[0]  # Atribui o primeiro valor da tupla a size
        message = connectionSocket.recv(1024)  # Recebe o restante
        message = unpack(f'>{size}s', message)[0]  # Atribui o primeiro valor da tupla a message
        message = message.decode()  # Transformas os bytes em string novamente
        decoded = decode(message, X)  # Retira a cifra de Cesar
        print(f'Sending to client: {decoded}')  # Mostra a mensagem decodificada que será enviada de volta
        connectionSocket.send(pack(f'>{size}s', decoded.encode()))
        connectionSocket.close()
    except connectionSocket.timeout as e:
        print(e)
        connectionSocket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = int(input('Insert the port: '))
    serverSocket.bind(('', port))
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        connectionSocket, addr = serverSocket.accept()                      # Aceita a conexão
        threading.Thread(target=thread, args=(connectionSocket,)).start()   # Abre uma thread para o cliente

if __name__ == '__main__':
    main()