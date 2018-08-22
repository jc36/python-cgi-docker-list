pipeline {
  agent any
  stages {
    stage('run docker') {
      steps {
        sh '''#docker stop pcdl
#docker rm pcdl
#docker rmi jc36/python-cgi-docker-list
sudo docker run --rm -p 8000:8000 --name pcdl --volume /var/run/docker.sock:/var/run/docker.sock --privileged jc36/python-cgi-docker-list'''
      }
    }
    stage('finish') {
      steps {
        echo 'Done!'
      }
    }
  }
}