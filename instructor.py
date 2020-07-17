class Instructor:
    def __init__(self, first_name='', last_name='',slack='', specialty='', cohort=''):
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.specialty = specialty
        self.cohort = cohort

    def assign_exercises(self, student, exercise_names):
        names = [exercise.name for exercise in exercise_names]
        student.assign_exercises(names)