import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
print('Digite o número da turma para iniciar sua chamada:')

msg = ''
client_code = 'teacher'

def getIdentifiedMsg(msg, client_code):
    return f'{msg},{client_code}'

while True:
    userInput = input()
    msg = str(userInput)
    encodedPackage = str.encode(getIdentifiedMsg(msg, client_code))
    client.send(encodedPackage)
    response = client.recv(1024)
    decoded_response = response.decode()
    print(decoded_response)
