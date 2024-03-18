# use an official python runtime
FROM python:3.9-slim

# set the working directory in the container
WORKDIR /app

# copy the 'app.py' file to the working directory
COPY app.py /app

# run the command to install the dependencies
RUN pip install flask psycopg2-binary Flask-SQLAlchemy Flask-Cors

# expose the port 5001
EXPOSE 5001

# define the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# command to run on container start
CMD ["flask", "run"]
