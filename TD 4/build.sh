# build.sh
#!/bin/bash

docker build -t app -f Dockerfile.app .
docker build -t db -f Dockerfile.db .