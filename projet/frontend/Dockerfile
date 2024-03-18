# use an official python runtime
FROM python:3.9-slim

# create a group and user to run our app
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# set the working directory in the container
WORKDIR /app

# run the command to install the dependencies
RUN pip install flask watchdog

# copy the application files to the working directory
COPY app.py /app
COPY templates /app/templates
COPY static /app/static
COPY hot_reload.py /app

# expose the port the app runs on
EXPOSE 5000

# define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# use HEALTHCHECK to allow Docker to verify the service is running
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

# switch to the user
USER appuser

# give execute permission to the hot_reload.py file
#RUN chmod +x hot_reload.py

# command to run on container start
CMD ["sh", "-c", "flask run & python hot_reload.py"]
