pipeline {
    agent { docker { image 'python:3.7-slim' } }
    stages {
        stage('build') {
            steps {
                echo 'Basic test'
                sh 'python --version'
            }
        }
    }
}
