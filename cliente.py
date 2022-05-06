from socket import *
from struct import *
import re

def encode(message):
    i = 0
    index = 0

    identifier = re.compile("^[a-z][a-z]*?[a-z]$")

    # Aceita apenas menssagens em letras minusculas e sem espaçamentos ou outros caracteres
    if not re.match(identifier, message):
        print('ERROR')
        quit()

    letter = message[0]
    encoded = ''
    while i < len(message):
        asciiNum = ord(letter)              # Retorna o valor ascii do caracter

        if asciiNum + 3 > 122:              # Se passar de z(122) voltamos ao inicio a(97)
            rest = (asciiNum + 3) % 122
            asciiNum = 96 + rest
        else:
            asciiNum = asciiNum + 3         # Soma o valor ascii na letra
        encoded += chr(asciiNum)            # Retorna o caracter correspondente a letra original
        i += 1
        if i < len(message):                 # Se chegar ao fim da string o mesage[i] não existe
            letter = message[i]
    return encoded

ip = input('Type the server IP: ')
port = int(input('Type the server port: '))
message = encode(input('Input one lowercase word: '))
size = int(input('Insert the string size: '))
# ip = 'localhost'
# port = 12000
# message = encode('stringdetest')
# size = 1

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ip, port))
print(f'Sending to server: {message}, {size}')
clientSocket.send(pack('>I', size))
clientSocket.send(message.encode())
decodedMessage = clientSocket.recv(1024).decode()
print(f'From server: {decodedMessage}')
clientSocket.close()

#           A fazer:
# Remover necessidade de .encode() se for obrigatorio
# Conseguir enviar size em pack('>i', size)
# Conseguir desligar o servidor se for obrigatorio
