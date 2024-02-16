-- init.sql
-- create the table
CREATE TABLE courses (course_id serial primary key, title varchar(100), description varchar(200), teacher varchar(100));
CREATE TABLE students (student_id serial primary key, fullname varchar(100), age int);
CREATE TABLE following (student_id int, course_id int, primary key(student_id, course_id));

-- insert some data
INSERT INTO courses (title, description, teacher) VALUES ('Math', 'Math course', 'Mr. Smith');
INSERT INTO courses (title, description, teacher) VALUES ('English', 'English course', 'Mrs. Johnson');
INSERT INTO courses (title, description, teacher) VALUES ('Science', 'Science course', 'Mr. Brown');
INSERT INTO students (fullname, age) VALUES ('John Doe', 20);
INSERT INTO students (fullname, age) VALUES ('Jane Doe', 19);
INSERT INTO students (fullname, age) VALUES ('Jim Doe', 18);
INSERT INTO following (student_id, course_id) VALUES (1, 1);
INSERT INTO following (student_id, course_id) VALUES (1, 2);
INSERT INTO following (student_id, course_id) VALUES (2, 2);
INSERT INTO following (student_id, course_id) VALUES (3, 3);

-- check the data
SELECT * FROM courses;
SELECT * FROM students;
SELECT * FROM following;