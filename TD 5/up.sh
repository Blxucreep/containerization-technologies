# up.sh
#!/bin/bash

docker run -d --name app --network my-tiny-network app
docker run -d --name db --network my-tiny-network db