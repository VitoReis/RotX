from socket import *
from struct import *
import re

def encode(message):
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

        if asciiNum + 3 > 122:              # Se passar de z(122) voltamos ao inicio a(97)
            remnant = (asciiNum + 3) % 122
            asciiNum = 96 + remnant
        else:
            asciiNum = asciiNum + 3         # Soma o valor ascii na letra
        encoded += chr(asciiNum)            # Retorna o caracter correspondente a letra original
        i += 1
        if i < len(message):                 # Se chegar ao fim da string o mesage[i] não existe
            letter = message[i]
    return encoded

def main():
    # ip = input('Type the server IP: ')
    # port = int(input('Type the server port: '))
    # message = encode(input('Input one lowercase word: '))
    # X = int(input('Insert one integer: '))
    ip = '127.0.0.1'
    port = 5000
    message = encode('stringdetest')
    size = len(message)
    X = 15

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((ip, port))
    # clientSocket.send(pack('>I', size))
    clientSocket.send(message.encode())
    # clientSocket.send(pack('>I', X))
    decodedMessage = clientSocket.recv(1024).decode()
    print(f'From server: {decodedMessage}')
    clientSocket.close()

if __name__ == '__main__':
    main()

#           A fazer:
# Remover necessidade de .encode() se for obrigatorio
# Conseguir desligar o servidor se for obrigatorio
# Enviar size, message e X junto
# Pq precisa de enviar size e o numero?
