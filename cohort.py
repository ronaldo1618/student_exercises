class Cohort:
    def __init__(self, name=''):
        self.name = name
        self.students = list()
        self.instructors = list()

    def assign_instructor(self, name):
        self.instructors.append(name)

    def assign_student(self, name):
        self.students.append(name)