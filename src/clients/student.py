import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
print('''
---------------[BEM VINDO]------------------

Olá Aluno,
Bem vindo ao sistema de registro de presença.

---------------------------------------------
''')

msg = ''
client_code = 'student'

def use_client_code(msg, client_code):
    return f'{msg},{client_code}'

while True:
    user_number = input('Informe seu número de matrícula: ')
    user_class = input('Informe o número da matéria em que deseja registrar presença: ')
    msg = str(user_number + '/' + user_class)
    encoded_package = str.encode(use_client_code(msg, client_code))
    client.send(encoded_package)
    response = client.recv(1024)
    decoded_response = response.decode()
    print(decoded_response)
