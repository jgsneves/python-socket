import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
print('Digite o seu número de matrícula para registrar presença:')

msg = ''
client_code = 'student'

def get_identified_msg(msg, client_code):
    return f'{msg},{client_code}'

while True:
    user_input = input()
    msg = str(user_input)
    encoded_package = str.encode(get_identified_msg(msg, client_code))
    client.send(encoded_package)
    response = client.recv(1024)
    decoded_response = response.decode()
    print(decoded_response)
