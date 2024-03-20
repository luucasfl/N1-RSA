from socket import *

# Nome                            RA
# Alessandro Matheus Toledo       082190007
# Gabriel Tadeu Sperche           082190012
# Lucas de Freitas Leal           082190025
# Murilo Moura Macedo             082190034


def encrypt(msg, e, N):
    return pow(int.from_bytes(msg.encode(), 'big'), e, N)

msg = 'The information security is of significant importance to ensure the privacy of communications'
bitLen = 4096 

# Comunicação com o server (Bob)
serverName = "192.168.56.1"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Recebimento da chave pública do server
P = clientSocket.recv(bitLen).decode().split('|')
e = int(P[0])
N = int(P[1])

# Criptografia e envio da mensagem
msgCifrada = str(encrypt(msg, e, N))
clientSocket.send(msgCifrada.encode())
print("Mensagem enviada para o server:", msgCifrada)
clientSocket.close()
