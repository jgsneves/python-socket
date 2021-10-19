import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
print('Digite o número da turma para iniciar sua chamada:')

msg = ''
clientCode = 'teacher'

def getIdentifiedMsg(msg, clientCode):
    return f'{msg},{clientCode}'

while True:
    userInput = input()
    msg = str(userInput)
    encodedPackage = str.encode(getIdentifiedMsg(msg, clientCode))
    client.send(encodedPackage)
    response = client.recv(1024)
    decoded_response = response.decode()
    print(decoded_response)
