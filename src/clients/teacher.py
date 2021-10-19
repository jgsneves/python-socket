import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

msg = ''
clientCode = 'teacher'

def getIdentifiedMsg(msg, clientCode):
    return f'{msg},{clientCode}'

while True:
    userInput = input()
    msg = str(userInput)
    encodedPackage = str.encode(getIdentifiedMsg(msg, clientCode))
    client.send(encodedPackage)