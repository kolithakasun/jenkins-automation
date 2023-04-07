# jenkins-automation

## Steps to deploy Jenkins
~~~
docker pull jenkins/jenkins
docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins
docker exec -it <container_id> bash
~~~

##
pip install --upgrade google-api-python-client