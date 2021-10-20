import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

print('''
---------------[BEM VINDO]------------------

Olá Professor,
Bem vindo ao sistema de registro de presença!

Neste sistema é possível:
- Abrir chamada de uma matéria;
- Encerrar a chamada da mesma;
- Consultar a lista de alunos presentes;

---------------------------------------------
''')
print('Digite o número da turma para iniciar/finalizar sua chamada:')

msg = ''
client_code = 'teacher'

def use_client_code(msg, client_code):
    return f'{msg},{client_code}'

while True:
    userInput = input()
    msg = str(userInput)
    encodedPackage = str.encode(use_client_code(msg, client_code))
    client.send(encodedPackage)
    response = client.recv(1024)
    decoded_response = response.decode()
    print(decoded_response)
