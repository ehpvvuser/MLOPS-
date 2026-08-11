pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f mlops-container || true'
                sh 'docker run -d --network host --name mlops-container mlops-app''
            }
        }

        stage('Test Application') {
            steps {
                sh 'curl http://localhost:5000'
            }
        }
    }
}
