## step 1: build the application
# use the golang alpine image
FROM golang:alpine as builder

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . .

# download the dependencies
RUN go mod download && go mod verify

# build the application
RUN go build -v -o /consumer

## step 2: run the application
# empty container
FROM scratch

# copy the binary from the builder stage to the alpine image
COPY --from=builder /consumer .

# expose port 8080
EXPOSE 8080

# run the application
CMD ["./consumer"]