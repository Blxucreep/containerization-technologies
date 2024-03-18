-- init-db.sql
-- create the table
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  sender TEXT NOT NULL,
  receiver TEXT NOT NULL,
  time TIMESTAMP NOT NULL,
  content TEXT NOT NULL
);
