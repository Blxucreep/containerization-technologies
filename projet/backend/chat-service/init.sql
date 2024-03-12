-- init.sql
-- create the table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(30) NOT NULL,
  password VARCHAR(30) NOT NULL
);
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  sender_id INTEGER NOT NULL,
  receiver_id INTEGER NOT NULL,
  message TEXT NOT NULL
);

-- insert some data
INSERT INTO users (username, password) VALUES ('alice', 'password');
INSERT INTO users (username, password) VALUES ('bob', 'password');
INSERT INTO messages (sender_id, receiver_id, message) VALUES (1, 2, 'Hello, Bob!');
INSERT INTO messages (sender_id, receiver_id, message) VALUES (2, 1, 'Hello, Alice!');

-- check the data
SELECT * FROM users;
SELECT * FROM messages;