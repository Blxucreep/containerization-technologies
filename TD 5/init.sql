-- init.sql
-- create the database
CREATE DATABASE test_db;

-- move to the database
\l test_db;

-- create the table
CREATE TABLE course (course_id serial primary key, title varchar(100), description varchar(200), teacher varchar(100));
CREATE TABLE student (student_id serial primary key, fullname varchar(100), age int);
CREATE TABLE following (student_id int, course_id int, primary key(student_id, course_id));

-- insert some data
INSERT INTO course (title, description, teacher) VALUES ('Math', 'Math course', 'Mr. Smith');
INSERT INTO course (title, description, teacher) VALUES ('English', 'English course', 'Mrs. Johnson');
INSERT INTO course (title, description, teacher) VALUES ('Science', 'Science course', 'Mr. Brown');
INSERT INTO student (fullname, age) VALUES ('John Doe', 20);
INSERT INTO student (fullname, age) VALUES ('Jane Doe', 19);
INSERT INTO student (fullname, age) VALUES ('Jim Doe', 18);
INSERT INTO following (student_id, course_id) VALUES (1, 1);
INSERT INTO following (student_id, course_id) VALUES (1, 2);
INSERT INTO following (student_id, course_id) VALUES (2, 2);
INSERT INTO following (student_id, course_id) VALUES (3, 3);

-- check the data
SELECT * FROM course;
SELECT * FROM student;
SELECT * FROM following;