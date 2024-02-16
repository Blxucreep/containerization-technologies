# use an official python runtime
FROM python:3.8-slim

# set the working directory in the container
WORKDIR /app

# copy the app.py file into the container at /app
COPY app.py /app

# install dependencies (here, it should install flask)
RUN pip install flask psycopg2-binary

# run app.py when the container launches
CMD ["python", "app.py"]