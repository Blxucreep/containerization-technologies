# up.sh
#!/bin/bash

docker run -d -p 8080:8080 --name app --network my-tiny-network app
docker run -d -p 5432:5432 --name db --network my-tiny-network db