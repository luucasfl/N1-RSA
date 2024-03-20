import sympy
import random
from socket import *

# Nome                            RA
# Alessandro Matheus Toledo       082190007
# Gabriel Tadeu Sperche           082190012
# Lucas de Freitas Leal           082190025
# Murilo Moura Macedo             082190034


def decrypt(msgCifrada, d, N):
    numbers = pow(msgCifrada, d, N)
    return numbers.to_bytes((numbers.bit_length() + 7) // 8, 'big').decode()

def gdc(a, b):
    while b:
        a, b = b, a % b
    return a

bitLen = 4096 

# Etapa 1 - Escolher p e q (números primos) para o cálculo de N = p.q
p = sympy.randprime(2**(bitLen//2 - 1), 2**(bitLen//2))
q = sympy.randprime(2**(bitLen//2 - 1), 2**(bitLen//2))
N = p * q

# Etapa 2 - Calcular a função totiente o(N) = (p-1).(q-1) 
totiente = (p - 1) * (q - 1)

# Etapa 3 - Escolha 1 < e < o(N), tal que e e o(N) sejam primos entre si
while True:
    e = random.randint(2, totiente - 1)
    if gdc(e, totiente) == 1:
        break

# Etapa 4 - Escolha d tal que e.d mod o(N) =1
d = sympy.mod_inverse(e, totiente)   

# Comunicação com o client (Alice)
serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)
print("Server aguardando resposta do client...\n")
connectionSocket, addr = serverSocket.accept()

# Envio da chave publica para o client
connectionSocket.send((str(e)+'|'+str(N)).encode())

# Recebimento e descriptografia da mensagem
msgCifrada = int(connectionSocket.recv(bitLen).decode())
msgDecifrada = decrypt(msgCifrada, d, N)
print("Mensagem recebida do client:", msgCifrada)
print("Mensagem descriptografada:", msgDecifrada)
connectionSocket.close()