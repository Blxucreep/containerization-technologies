# use the golang alpine image
FROM golang:alpine

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . .

# expose port 8080
EXPOSE 8080

# run the application
CMD ["go", "run", "main.go"]