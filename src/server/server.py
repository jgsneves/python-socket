from array import array
import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()
print('Servidor está escutando...')

connection, client = server.accept()
print('Cliente conectado: ', client)

currentClass = ''
responseMessage = ''
presentStudents = []

def handleTeacherMsg(message: str, currentClass: str):
    if currentClass == '':
        currentClass = message
        return f'A chamada da turma {currentClass} está ativa!'
    else:
        if message == currentClass:
            return f'A chamada da turma {currentClass} foi encerrada!'
        else:
            return 'Comando não encontrado'

def handleStudentMsg(message: str):
    # TO DO
    pass

def getResponse(decodedData: tuple, currentClass: str):
    clientMessage: str = decodedData[0]
    clientCode: str = decodedData[1]
    if clientCode == 'teacher':
        return handleTeacherMsg(clientMessage, currentClass)
    else:
        handleStudentMsg(clientMessage)

while True:
    data = connection.recv(1024)
    decodedData = data.decode()
    response = getResponse(decodedData, currentClass)