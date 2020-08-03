DELETE FROM cohorts;
DELETE FROM students;
DELETE FROM instructors;
DELETE FROM exercises;
DELETE FROM student_exercises;

DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS student_exercises;

CREATE TABLE cohorts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE students (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL UNIQUE,
    slack_handle TEXT NOT NULL UNIQUE,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY(cohort_id) REFERENCES cohorts(id)
);

CREATE TABLE instructors (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL UNIQUE,
    slack_handle TEXT NOT NULL UNIQUE,
    specialty TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY(cohort_id) REFERENCES cohort(id)
);

CREATE TABLE exercises (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    language TEXT NOT NULL
);

CREATE TABLE student_exercises (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id)
    FOREIGN KEY(exercise_id) REFERENCES exercises(id)
    FOREIGN KEY(instructor_id) REFERENCES instructors(id)
);

INSERT INTO cohorts (name)
VALUES ('cohort 40');

INSERT INTO cohorts (name)
VALUES ('cohort 38');

INSERT INTO cohorts (name)
VALUES ('cohort 42');

INSERT INTO exercises (name, language)
VALUES ('Kandy Korner', 'Javascript');

INSERT INTO exercises (name, language)
VALUES ('Student Exercises', 'Python');

INSERT INTO exercises (name, language)
VALUES ('Petting Zoo', 'Python');

INSERT INTO exercises (name, language)
VALUES ('Daily Journal', 'Javascript');

INSERT INTO exercises (name, language)
VALUES ('Music History', 'SQL');

INSERT INTO instructors (first_name, last_name, slack_handle, specialty, cohort_id)
SELECT 'Joe', 'Shepherd', 'joes', 'Wisdom +3', cohorts.id
FROM cohorts
WHERE cohorts.name like '%40%';

INSERT INTO instructors (first_name, last_name, slack_handle, specialty, cohort_id)
SELECT 'Bryan', 'Nilsen', 'brys', 'Dadjokes +3', cohorts.id
FROM cohorts
WHERE cohorts.name like '%38%';

INSERT INTO instructors (first_name, last_name, slack_handle, specialty, cohort_id)
SELECT 'Madi', 'Peper', 'madis', 'Dadjokes +3', cohorts.id
FROM cohorts
WHERE cohorts.name like '%42%';

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Gerald', 'Geoff', 'idk', cohorts.id
FROM cohorts
WHERE cohorts.name like '%42%';

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Geoff', 'Gerald', 'idk2', cohorts.id
FROM cohorts
WHERE cohorts.name like '%42%';

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Tim', 'Tony', 'timone', cohorts.id
FROM cohorts
WHERE cohorts.name like '%40%';

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Tony', 'Tim', 'tony', cohorts.id
FROM cohorts
WHERE cohorts.name like '%40%';

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Shae', 'Peper', 'shae', cohorts.id
FROM cohorts
WHERE cohorts.name like '%38%';

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'geoff', 'geoff', 'mynamegeoff', cohorts.id
FROM cohorts
WHERE cohorts.name like '%38%';

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
SELECT 'Ronnie', 'Whoknows', 'ronnieyouknow', cohorts.id
FROM cohorts
WHERE cohorts.name like '%40%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Ronnie%'
AND exercises.name like '%Kandy%'
AND instructors.first_name like '%Joe%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Ronnie%'
AND exercises.name like '%Daily%'
AND instructors.first_name like '%Madi%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Gerald%'
AND exercises.name like '%Kandy%'
AND instructors.first_name like '%Bryan%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Gerald%'
AND exercises.name like '%Petting%'
AND instructors.first_name like '%Bryan%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Geoff%'
And students.last_name like '%Gerald%'
AND exercises.name like '%Kandy%'
AND instructors.first_name like '%Joe%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Geoff%'
And students.last_name like '%Gerald%'
AND exercises.name like '%Daily%'
AND instructors.first_name like '%Madi%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Tim%'
AND exercises.name like '%Daily%'
AND instructors.first_name like '%Bryan%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Tony%'
AND exercises.name like '%Petting%'
AND instructors.first_name like '%Joe%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Tony%'
AND exercises.name like '%Daily%'
AND instructors.first_name like '%Madi%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Tim%'
AND exercises.name like '%Petting%'
AND instructors.first_name like '%Bryan%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Shae%'
AND exercises.name like '%Studen%'
AND instructors.first_name like '%Joe%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Shae%'
AND exercises.name like '%Kandy%'
AND instructors.first_name like '%Madi%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Geoff%'
AND students.last_name like '%geoff%'
AND exercises.name like '%Music%'
AND instructors.first_name like '%Bryan%';

INSERT INTO student_exercises (student_id, exercise_id, instructor_id)
SELECT students.id, exercises.id, instructors.id
FROM students, exercises, instructors
WHERE students.first_name like '%Geoff%'
AND students.last_name like '%geoff%'
AND exercises.name like '%Petting%'
AND instructors.first_name like '%Joe%';