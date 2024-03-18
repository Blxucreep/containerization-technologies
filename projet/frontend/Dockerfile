# Use an official Python runtime
FROM python:3.9-slim

# Create a group and user to run our app
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set the working directory in the container
WORKDIR /app

# Run the command to install the dependencies
# Ensure you pin the version of Flask to a specific version you've tested with
RUN pip install --no-cache-dir flask==2.1.0

# Copy the application files to the working directory
COPY app.py /app
COPY templates /app/templates
COPY static /app/static

# Expose the port the app runs on
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Use HEALTHCHECK to allow Docker to verify the service is running
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

# Switch to the user
USER appuser

# Command to run on container start
CMD ["flask", "run"]
