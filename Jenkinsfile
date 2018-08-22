pipeline {
  agent any
  stages {
    stage('push to git') {
      steps {
        sh '''cd project/python-cgi-docker-list
#touch touchfile
#git add *
git commit -am "newCommit"
git remote set-url origin git@github.com:jc36/python-cgi-docker-list
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
docker rm pcdl
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