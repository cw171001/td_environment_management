pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'Building..'
          }
        }
        stage('Directory') {
          steps {
            bat(script: 'test.py', returnStatus: true, returnStdout: true)
          }
        }
        stage('Directory') {
          steps {
            bat(script: 'jenkins/test.py', returnStatus: true, returnStdout: true)
          }
        }
        stage('Sing') {
          steps {
            echo 'Building..'
          }
        }
      }
    }
    stage('Test') {
      steps {
        echo 'Testing..'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
    stage('Cook') {
      steps {
        echo 'Cook....'
      }
    }
    stage('Supper') {
      steps {
        sleep 10
      }
    }
  }
}