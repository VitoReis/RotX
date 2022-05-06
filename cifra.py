import re

def encode():
    i = 0
    index = 0
    mesage = 'helloworld'
    print('MENSAGE\n' + mesage)

    identifier = re.compile("^[a-z][a-z]*?[a-z]$")

    # Aceita apenas menssagens em letras minusculas e sem espaçamentos ou outros caracteres
    if not re.match(identifier, mesage):
        print('ERROR')
        quit()

    X = int(input('Digite o numero X da criptografia: '))
    letter = mesage[0]
    encoded = ''
    while i < len(mesage):
        asciiNum = ord(letter)              # Retorna o valor ascii do caracter

        if asciiNum + X > 122:              # Se passar de z(122) voltamos ao inicio a(97)
            rest = (asciiNum + X) % 122
            asciiNum = 96 + rest
        else:
            asciiNum = asciiNum + X         # Soma o valor ascii na letra
        encoded += chr(asciiNum)            # Retorna o caracter correspondente a letra original
        i += 1
        if i < len(mesage):                 # Se chegar ao fim da string o mesage[i] não existe
            letter = mesage[i]

    print('ENCODED\n' + encoded)
    decode(X, encoded)

def decode(X, encoded):
    i = 0
    index = 0
    X = X                           # Trocar pelo X do cliente
    letter = encoded[0]
    mesage = ''

    while i < len(encoded):
        asciiNum = ord(letter)              # Retorna o valor ascii do caracter
        if asciiNum - X < 97:               # Se menor que a(97) voltamos ao fim z(122)
            rest = 97 - (asciiNum - X)
            asciiNum = 123 - rest
        else:
            asciiNum = asciiNum - X         # Subtrai o valor ascii na letra
        mesage += chr(asciiNum)            # Retorna o caracter correspondente a letra codificada
        i += 1
        if i < len(encoded):                 # Se chegar ao fim da string o mesage[i] não existe
            letter = encoded[i]
    print('DECODED\n' + mesage)