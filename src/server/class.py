class ClassService:
    def __init__(self, current_class, response_message, present_students) -> None:
        current_class = current_class
        response_message = response_message
        present_students = present_students

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