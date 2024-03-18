# use an official python runtime
FROM python:3.9-slim

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory and run the command to install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the 'app.py' file to the working directory
COPY app.py .

# expose the port 5002
EXPOSE 5002

# define the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5002

# command to run on container start
CMD ["flask", "run"]
