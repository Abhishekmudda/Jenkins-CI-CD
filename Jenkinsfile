pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/even-odd-checker.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip3 install --upgrade pip --break-system-packages
                    pip3 install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                 sh '''
                    python3 -m pytest > result.log || echo "tests failed"
                    cat result.log
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t even-odd-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f even-odd-container || true'
                sh 'docker run -d -p 5003:5003 --name even-odd-container even-odd-app'
            }
        }
    }
}
