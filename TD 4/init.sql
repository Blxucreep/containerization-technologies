-- init.sql
-- create the database
CREATE DATABASE test_db;

-- move to the database
\l test_db;

-- create the table
CREATE TABLE test_table (id serial primary key, description varchar(255));

-- insert some data
INSERT INTO test_table (description) VALUES ('test1'), ('test2'), ('test3');

-- check the data
SELECT * FROM test_table;