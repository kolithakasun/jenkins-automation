#!/bin/bash
docker pull jenkins/jenkins
docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins
docker exec -it c778d75bd798 bash
