pipeline {
  agent any
  stages {
    stage('push to git') {
      steps {
        sh '''git commit -am "newCommit"
git push -u origin master'''
      }
    }
    stage('wait') {
      steps {
        sleep(unit: 'MINUTES', time: 5)
        echo 'wait 5 minutes until building'
      }
    }
    stage('run docker') {
      steps {
        sh '''docker stop pcdl
dcoker rm pcdl
docker rmi jc36/python-cgi-docker-list
docker run --rm -p 8000:8000 --name pcdl --volume /var/run/docker.sock:/var/run/docker.sock --privileged jc36/python-cgi-docker-list'''
      }
    }
    stage('finish') {
      steps {
        echo 'Done!'
      }
    }
  }
}