from datetime import datetime

from models.classtype import ClassType

class Service:
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
