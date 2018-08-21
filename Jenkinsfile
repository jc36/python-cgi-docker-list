pipeline {
  agent any
  stages {
    stage('1') {
      parallel {
        stage('1') {
          steps {
            echo '1111'
          }
        }
        stage('1.1') {
          steps {
            echo '1.1'
          }
        }
      }
    }
    stage('2') {
      parallel {
        stage('2') {
          agent any
          steps {
            sleep 1
          }
        }
        stage('2.1') {
          steps {
            echo '2.1'
          }
        }
      }
    }
    stage('3') {
      steps {
        echo 'finish'
      }
    }
  }
}