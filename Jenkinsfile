pipeline {
  agent any
  stages {
    stage('run docker') {
      steps {
        sh '''sudo docker stop pcdl
sudo docker rm pcdl
sudo docker rmi jc36/python-cgi-docker-list
sudo docker run -d -p 8000:8000 --name pcdl --volume /var/run/docker.sock:/var/run/docker.sock --privileged jc36/python-cgi-docker-list'''
      }
    }
    stage('finish') {
      steps {
        echo 'Done!'
      }
    }
  }
}