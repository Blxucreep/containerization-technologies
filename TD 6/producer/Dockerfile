## step 1: build the application
# use the golang alpine image
FROM golang:1.19-alpine as builder

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY go.sum go.mod main.go ./

# download the dependencies
RUN go mod download

# build the application
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /producer

## step 2: run the application
# use the alpine image
FROM alpine:3.14

# set the working directory in the container
WORKDIR /

# copy the binary from the builder stage to the alpine image
COPY --from=builder /producer ./

# expose port 8080
EXPOSE 8080

# run the application
CMD ["/producer"]