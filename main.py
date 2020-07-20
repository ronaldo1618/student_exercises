from exercise import Exercise
from cohort import Cohort
from NSSPerson import Student
from NSSPerson import Instructor

# Creating Exercises
student_exercise = Exercise('Student Exercise', 'Python')
petting_zoo = Exercise('Petting Zoo', 'Python')
kandy_korner = Exercise('Kandy Korner', 'Javascript')
daily_journal = Exercise('Daily Journal', 'Javascript')

# Creating Cohorts
cohort_40 = Cohort('cohort 40')
cohort_41= Cohort('cohort 41')
cohort_42 = Cohort('cohort 42')

# Creating Students
ronnie = Student('Ronald', 'Lankford', 'ronnielankford', 'cohort 40')
geoff = Student('Geoff', 'Slater', 'mynamegeoff', 'cohort 41')
mark = Student('Mark', 'Kagoan', 'markymark', 'cohort 40')
shae = Student('Shae', 'Choate', 'shadeofshae', 'cohort 42')

# Creating Instructors
joe = Instructor('Joe', 'Shepherd', 'joe', 'dad jokes', 'cohort 40')
bry = Instructor('Bryan', 'Nilsen', 'bry', 'dad jokes', 'cohort 41')
madi = Instructor('Madi', 'Peper', 'madi', 'dad jokes', 'cohort 42')

# Assigning Instructors to Cohorts
cohort_40.assign_instructor(joe)
cohort_41.assign_instructor(bry)
cohort_42.assign_instructor(madi)

# Assigning Students to Cohorts
cohort_40.assign_student(ronnie)
cohort_40.assign_student(mark)
cohort_41.assign_student(geoff)
cohort_42.assign_student(shae)

# Instructors Assigning Exercises
joe.assign_exercises(ronnie, [student_exercise, petting_zoo])
joe.assign_exercises(mark, [kandy_korner, daily_journal, petting_zoo, student_exercise])
bry.assign_exercises(geoff, [student_exercise, petting_zoo])
madi.assign_exercises(shae, [kandy_korner, daily_journal])

# Find a better way
students = list()
exercises = list()
students.extend([ronnie, mark, geoff, shae])
exercises.extend([student_exercise.name, petting_zoo.name, kandy_korner.name, daily_journal.name])

for student in students:
    working_on_exercises = list(set(student.exercises).intersection(set(exercises)))
    working_on_exercises[-2] += ',' if len(working_on_exercises) > 2 else ''
    print(f'{student.first_name} is working on {", ".join(working_on_exercises[:-1])} and {working_on_exercises[-1]}.')
