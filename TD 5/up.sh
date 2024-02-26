# up.sh
#!/bin/bash

# create the my-tiny-network if it doesn't exist
docker network create my-tiny-network || true

# create the db-vol if it doesn't exist
docker volume create db-vol || true

docker run -d -p 8080:8080 --name app --network my-tiny-network app
docker run -d -p 5432:5432 --name db --network my-tiny-network -v db-vol:/data -e PGDATA=/data db