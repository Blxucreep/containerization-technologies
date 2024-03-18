# use an official python runtime
FROM python:3.9-slim

# set the working directory in the container
WORKDIR /app

# run the command to install the dependencies
RUN pip install flask

# copy the 'app.py' file to the working directory
COPY app.py /app

# copy the 'templates' directory to the working directory
COPY templates /app/templates

# copy the 'static' directory to the working directory
COPY static /app/static

# expose the port 5000
EXPOSE 5000

# define the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# command to run on container start
CMD ["flask", "run"]
