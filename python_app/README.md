## Pre Run
1. enter containers: `docker exec -it spark-master /bin/bash`
2. execute: `apk add py-numpy`
3. exit: `exit`
4. repeat 1-3 for: spark-master, all spark-worker-


## Running the application
1. `docker-compose run app /bin/bash`
2. `./template.sh`
3. `cat home/results/part-00000`

## Spark panel: 0.0.0.0:8080
