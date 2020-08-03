import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}.'

class Instructor():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}.'

class Cohort():

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'{self.name}'

class Exercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} is an exercise in the {self.language} language.'

class Javascript_exercise():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name} is an exercise in the Javascript language.'

class Python_exercise():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name} is an exercise in the Python language.'

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/ronnie/workspace/python/studentExercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from Students s
            join Cohorts c on s.cohort_id = c.id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.id,
                i.first_name,
                i.last_name,
                i.slack_handle,
                i.cohort_id,
                c.name
            from Instructors i
            join Cohorts c on i.cohort_id = c.id
            order by i.cohort_id
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)

    def all_cohorts(self):

        '''Retrieve all cohorts'''

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
            db_cursor = conn.cursor()

            db_cursor.execute('''
            SELECT c.id,
            c.name
            FROM cohorts c
            ''')

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

    def all_exercises(self):

         '''Display all exercises'''

         with sqlite3.connect(self.db_path) as conn:
             conn.row_factory = lambda cursur, row: Exercise(row[1], row[2])
             db_cursor = conn.cursor()

             db_cursor.execute('''
             SELECT e.id,
             e.name,
             e.language
             FROM exercises e
             ''')

             all_exercises = db_cursor.fetchall()

             for exercise in all_exercises:
                 print(exercise)

    def all_javascript_exercises(self):

         '''Display all javascript exercises'''

         with sqlite3.connect(self.db_path) as conn:
             conn.row_factory = lambda cursur, row: Javascript_exercise(row[1])
             db_cursor = conn.cursor()

             db_cursor.execute('''
             SELECT e.id,
             e.name
             FROM exercises e
             WHERE e.language like '%Javascript%'
             ''')

             all_javascript_exercises = db_cursor.fetchall()

             for exercise in all_javascript_exercises:
                 print(exercise)

    def all_python_exercises(self):

         '''Display all python exercises'''

         with sqlite3.connect(self.db_path) as conn:
             conn.row_factory = lambda cursur, row: Python_exercise(row[1])
             db_cursor = conn.cursor()

             db_cursor.execute('''
             SELECT e.id,
             e.name
             FROM exercises e
             WHERE e.language like '%Python%'
             ''')

             all_python_exercises = db_cursor.fetchall()

             for exercise in all_python_exercises:
                 print(exercise)

    def students_and_exercises(self):

        ''' Display all students and their associated exercises'''
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.id exercise_id,
                    e.name,
                    s.id,
                    s.first_name,
                    s.last_name
                from Exercises e
                join student_exercises se on se.exercise_id = e.id
                join Students s on s.id = se.student_id
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')

    def student_workload(self):

        '''Display student workload'''

        students_exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.id student_id,
                    e.name,
                    s.id,
                    s.first_name,
                    s.last_name
                from Exercises e
                join student_exercises se on se.exercise_id = e.id
                join Students s on s.id = se.student_id
            """)
        
            dataset = db_cursor.fetchall()

            for row in dataset:
                student_id = row[0]
                exercise_name = row[1]
                exercise_id = row[2]
                student_name = f'{row[3]} {row[4]}'

            for row in dataset:
                student_id = row[0]
                exercise_name = row[1]
                exercise_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if student_name not in students_exercises:
                    students_exercises[student_name] = [exercise_name]
                else:
                    students_exercises[student_name].append(exercise_name)

            for student_name, exercises in students_exercises.items():
                print(student_name, 'is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')

    def instructors_assigned_exercises(self):

        '''Display exercises assigned by instructors'''

        instructors_exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.id instructor_id,
                    e.name,
                    i.id,
                    i.first_name,
                    i.last_name
                from Exercises e
                join student_exercises se on se.exercise_id = e.id
                join Instructors i on i.id = se.instructor_id
            """)
        
            dataset = db_cursor.fetchall()

            for row in dataset:
                instructor_id = row[0]
                exercise_name = row[1]
                exercise_id = row[2]
                instructor_name = f'{row[3]} {row[4]}'

            for row in dataset:
                instructor_id = row[0]
                exercise_name = row[1]
                exercise_id = row[2]
                instructor_name = f'{row[3]} {row[4]}'

                if instructor_name not in instructors_exercises:
                    instructors_exercises[instructor_name] = [exercise_name]
                else:
                    instructors_exercises[instructor_name].append(exercise_name)

            for instructor_name, exercises in instructors_exercises.items():
                print(instructor_name, 'assigned the following exercises:')
                for exercise in exercises:
                    print(f'\t* {exercise}')




reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.all_javascript_exercises()
reports.all_python_exercises()
reports.all_instructors()
reports.students_and_exercises()
reports.student_workload()
reports.instructors_assigned_exercises()