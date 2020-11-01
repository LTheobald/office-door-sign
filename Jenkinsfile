pipeline {
    agent { docker { image 'python:3.7-slim' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}