# jenkins-automation
This `file_upload.py` can be used to upload files within the uploads directory to Sharepoint.


## Steps to deploy Jenkins
~~~
docker pull jenkins/jenkins
docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins
docker exec -it <container_id> bash
~~~

## Install Dependancies
~~~
pip3 install -r requirement.txt
~~~

## Steps to Manually Run
~~~
python3 file_upload.py $USRNAME $PASSWORD $FILE_NAME
~~~