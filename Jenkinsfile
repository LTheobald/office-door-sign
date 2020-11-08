pipeline {
  agent { docker { image 'python:3.7-slim' } }
  stages {
    stage('Build dependencies') {
      steps {
        sh 'apt install -y python3-dev python3-rpi.gpio python3-pil'
        sh 'pip install --upgrade pip setuptools wheel'
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
