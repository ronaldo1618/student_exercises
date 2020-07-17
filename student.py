class Student:
    def __init__(self, first_name='', last_name='', slack='', cohort=''):
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.cohort = cohort
        self.exercises = list()

    def assign_exercises(self, assigned_exercises):
        self.exercises.extend(assigned_exercises)