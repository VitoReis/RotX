from socket import *
from struct import *
import re
import socket
import sys

def encode(message, X):
    i = 0
    identifier = re.compile("^[a-z]+$")

    # Aceita apenas menssagens em letras minusculas e sem espaçamentos ou outros caracteres
    if not re.match(identifier, message):
        print('Encode error: Invalid string')
        quit()

    letter = message[0]
    encoded = ''
    while i < len(message):
        asciiNum = ord(letter)              # Retorna o valor ascii do caracter

        if asciiNum + X > 122:              # Se passar de z(122) voltamos ao inicio a(97)
            remnant = (asciiNum + X) % 122
            asciiNum = 96 + remnant
        else:
            asciiNum = asciiNum + X         # Soma o valor ascii na letra
        encoded += chr(asciiNum)            # Retorna o caracter correspondente a letra original
        i += 1
        if i < len(message):                 # Se chegar ao fim da string o mesage[i] não existe
            letter = message[i]
    return encoded

def main():
    if len(sys.argv) == 5:
        ip = sys.argv[1]
        port = int(sys.argv[2])
        message = sys.argv[3]
        X = int(sys.argv[4])
    else:
        ip = input('Type the server IP: ')
        port = int(input('Type the server port: '))
        message = input('Input one lowercase word: ')
        X = int(input('Insert the integer of the cipher: '))

    message = encode(message, X)        # Codifica a mensagem
    size = len(message)                 # Guarda o tamanho da string para o pack e unpack
    message = message.encode()          # Transforma a string em bytes

    clientSocket = socket.socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((ip, port))
    clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, 15)      # Define o timeout de 15 seg
    clientSocket.send(pack(f'>II{size}s', X, size, message))
    decodedMessage = unpack(f'{size}s', clientSocket.recv(1024))[0].decode()
    print(f'From server: {decodedMessage}')
    clientSocket.close()

if __name__ == '__main__':
    main()