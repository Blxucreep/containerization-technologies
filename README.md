# Containerization Technologies

Here the repository containing all the practical works done during the course of Containerization Technologies (S8).

## TD 1: Making our first container

You are going to make a container with the latest Ubuntu image, present in Docker Registry.

Use it, by trying some commands inside of this instance!

Document how you proceed along with screenshots of every step in a PDF.

In this document explain with your own words, which components of Docker you used.

Bonus:
- Clean the docker container your machine (one by one).
- Explain the difference between the docker client and the docker daemon.
- Explain what is the docker socket, and why using `chmod 666` on it is a bad idea.

## TD 2: Create a simple web server

Create a Dockerfile that sets up a web server (such as Apache or Nginx) and serves a simple HTML page. You may make other files if needed.

Build and run the container, and access the web page in a browser to verify that it's working.

Document all steps and explain in detail all components you used. 

Bonus: 
- Show that the webpage is accessible using only your terminal.
- Display the logs of a container.
- Add resource limitation (cpu/ram).
- If you create an Nginx web server, do the same thing with an Apache; and vice-versa.

## TD 3: Containerize a simple application

Take/make a simple application, such as a Python script, and create a Dockerfile that packages it into a container (it should need dependencies/extenal libraries).

Build an image of it, push it into the public registry (Docker hub).

Run the container and verify that the application works as expected.

Ask someone to try your image on their own PC.

Document all steps and explain in detail all components you used.

Bonus:
- Have the smallest possible image size.
- Run a linter on the Dockerfile.
- Explain the difference between ADD and COPY in a Dockerfile.
- Make the container run without sudo rights.
- Run a secure scan on the container and take it into account.
- Add your code on a public GitHub repository.