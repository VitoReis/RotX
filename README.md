# RotX
&nbsp;&nbsp;&nbsp;Esta é uma aplicação cliente-servidor, onde o cliente se conecta a um servidor e envia um string de texto criptografado, e o servidor recebe a strings do clientes e retorna uma versão decodificada do mesmo.
# Cifra de César
&nbsp;&nbsp;&nbsp;O seu princípio de operação é escolher um certo inteiro X e trocar cada caractere do string pelo caractere X posições à frente no alfabeto.

&nbsp;&nbsp;&nbsp;As funções **encode** e **decode** recebem o X escolhido pelo usuario e codificam/decodificam as mensagens, transformando as letras em codigo ASCII, pulando ou voltando X caracteres e retransformando o codigo ASCII em letras novamente.
#Programa Cliente
&nbsp;&nbsp;&nbsp;Ao ser iniciado, o programa cliente estabelece uma conexão com o servidor com timeout de 15 segundos, envia uma mensagem codificada na cifra de César, juntamente com o tamanho da string e o valor X, em network byte order e aguarda que o servidor devolva a string decodificada.
#Programa Servidor
&nbsp;&nbsp;&nbsp;O servidor recebe como parametro sua porta, ao iniciar ele aguarda uma conexão, quando esta é estabelecida ele cria uma thread para atende-la.

&nbsp;&nbsp;&nbsp;A thread do servidor espera que o cliente envie o valor de X, o tamanhno da string e por fim uma string, assim ele desempacota uma a uma, decodifica a mensagem, e envia de volta ao cliente.
