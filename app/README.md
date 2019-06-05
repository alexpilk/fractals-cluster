## Pre Run
1. enter containers: 'docker exec -it spark-master /bin/bash'
2. execute: 'apk add py-numpy'
3. exit: 'exit'
4. repeat 1-3 for: spark-master, all spark-worker-<number>

## Running the application
1. Run app container: `docker-compose run app /bin/bash`
2. execute: `./template.sh`
3. outside container, copy fractal to local: `docker cp <container_id>:fraktal.png ./fractal.png`

## Spark panel: 0.0.0.0:8080 

