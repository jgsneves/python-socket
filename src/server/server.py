import socket
import threading
from datetime import datetime

class ClassType:
    def __init__(self, number: str) -> None:
        self.number = number
        self.is_opened = False
        self.present_students = []

    def open(self):
        self.is_opened = True

    def close(self):
        self.is_opened = False

    def add_student(self, student_number):
        self.present_students.append(student_number)

    def remove_student(self, student_number):
        self.present_students.remove(student_number)

    def is_student_present(self, student_number):
        for student in self.present_students:
            if student == student_number:
                return True
        return False

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
        self.active_classes = []

    def add_class(self, class_obj):
        self.active_classes.append(class_obj)

    def remove_class(self, class_number):
        for item in self.active_classes:
            if item.number == class_number:
                self.active_classes.remove(item)

    def is_class_active(self, class_number):
        for item in self.active_classes:
            if item.number == class_number:
                return True
        return False

    def get_class_present_students(self, class_number):
        for item in self.active_classes:
            if item.number == class_number:
                return item.present_students

    def handle_teacher_message(self, message: str):
        currentDateAndTime = datetime.now().strftime("%d/%m/%Y às %H:%M")

        if self.is_class_active(message):
            present_students = self.get_class_present_students(message)
            self.remove_class(message)
            return f'A chamada da turma {message} foi encerrada em {currentDateAndTime}! Os seguintes alunos registraram presença: {present_students}'
        else:
            new_class = ClassType(message)
            self.add_class(new_class)
            return f'A chamada da turma {message} foi ativada em {currentDateAndTime}!'

    def handle_student_message(self, message: str):
        currentDateAndTime = datetime.now().strftime("%d/%m/%Y às %H:%M")
        student_infos = message.split('/')
        student_number = student_infos[0]
        class_number = student_infos[1]

        if self.is_class_active(class_number):
            for item in self.active_classes:
                if item.number == class_number:
                    item.add_student(student_number)
                break
            return f'Presença registrada com sucesso na turma {class_number} em {currentDateAndTime}!'
        else:
            return f'Esta turma não está com presença ativa. Solicitação rejeitada em {currentDateAndTime}'

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
