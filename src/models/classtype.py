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
