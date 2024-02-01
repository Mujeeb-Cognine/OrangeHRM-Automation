pipeline {
    agent any

    environment {
        CHROME_DRIVER_VERSION = '121.0.6167.140' // Update with the latest version
        PYTHON_VERSION = '3.12.1'  // Update with your Python version
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh "python${PYTHON_VERSION} -m pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests and Generate HTML Report') {
            steps {
                script {
                    sh "pytest --browser_name chrome --environment default_env --html=report.html"
                }
                publishHTML(target: [allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '.', reportFiles: 'report.html'])
            }
        }
    }
}
