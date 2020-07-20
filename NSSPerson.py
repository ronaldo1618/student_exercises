class NSSPerson():
    def __init__(self, first_name, last_name, slack, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.cohort = cohort

class Instructor(NSSPerson):
    def __init__(self, first_name='', last_name='',slack='', specialty='', cohort=''):
        super().__init__(first_name, last_name, slack, cohort)
        self.specialty = specialty

    def assign_exercises(self, student, exercise_names):
        names = [exercise.name for exercise in exercise_names]
        student.exercises.extend(names)

class Student(NSSPerson):
    def __init__(self, first_name='', last_name='', slack='', cohort=''):
        super().__init__(first_name, last_name, slack, cohort)
        self.exercises = list()