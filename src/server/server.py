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

class ClassService:
    def __init__(self, current_class, response_message, present_students) -> None:
        self.current_class = current_class
        self.response_message = response_message
        self.present_students = present_students

    def handle_teacher_message(self, message: str):
        if self.current_class == '':
            self.current_class = message
            return f'A chamada da turma {self.current_class} está ativa!'
        else:
            if message == self.current_class:
                return f'A chamada da turma {self.current_class} está encerrada!'
            else:
                return 'Comando inválido!'

    def handle_student_message(self):
        pass

    def get_response(self, decoded_data: str):
        message_list = decoded_data.split(',')
        client_message: str = message_list[0]
        client_code: str = message_list[1]
        if client_code == 'teacher':
            return self.handle_teacher_message(client_message)
        else:
            self.handle_student_message(client_code)

initial_class = ''
initial_response = ''
initial_present_students = []

new_service = ClassService(initial_class, initial_response, initial_present_students)

while True:
    data = connection.recv(1024)
    decodedData = data.decode()
    response = new_service.get_response(decodedData)
    print(response)