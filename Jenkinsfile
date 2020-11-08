pipeline {
  agent { docker { image 'python:3.7-slim' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('test') {
      steps {
        echo 'Begin tests'
        // sh 'python test.py'
      }
    }
  }
}
