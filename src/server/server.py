import socket
import threading
from datetime import datetime

class Server:
    def __init__(self, class_service) -> None:
        self.PORT = 5050
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.ADDRESS = (self.HOST, self.PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.service = class_service

    def run(self):
        self.server.bind(self.ADDRESS)
        self.server.listen()
        print('Servidor está escutando...')
        while True:
            connection, client = self.server.accept()
            print('Cliente conectado: ', client)
            thread = threading.Thread(target=self.handle_connection, args=(connection, client))
            thread.start()

    def handle_connection(self, connection: socket, _):
        while True:
            data: bytes = connection.recv(1024)
            decoded_data = data.decode()
            response: str = self.service.handle_message(decoded_data)
            print(response)
            encoded_response = response.encode()
            connection.send(encoded_response)


class ClassService:
    def __init__(self) -> None:
        self.current_class = ''
        self.present_students = []
    
    def is_student_present(self, student: str):
        if self.present_students.count(student) == 0:
            return False
        else:
            return True

    def handle_teacher_message(self, message: str):
        currentDateAndTime = datetime.now().strftime("%d/%m/%Y às %H:%M")
        if self.current_class == '':
            self.current_class = message
            return f'A chamada da turma {self.current_class} foi ativada em {currentDateAndTime}!'
        else:
            if message == self.current_class:
                class_name = self.current_class
                self.current_class = ''
                return f'A chamada da turma {class_name} foi encerrada em {currentDateAndTime}! Os seguintes alunos registraram presença: {self.present_students}'
            else:
                return 'Comando inválido!'

    def handle_student_message(self, student_number: str):
        if self.is_student_present(student_number):
            return f'Você já marcou presença!'
        else:
            self.present_students.append(student_number)
            return f'Aluno {student_number} registrou presença!'

    def handle_message(self, decoded_data: str):
        message_list = decoded_data.split(',')
        client_message: str = message_list[0]
        client_code: str = message_list[1]
        if client_code == 'teacher':
            return self.handle_teacher_message(client_message)
        else:
            return self.handle_student_message(client_message)

class_service = ClassService()

new_server = Server(class_service)

new_server.run()
