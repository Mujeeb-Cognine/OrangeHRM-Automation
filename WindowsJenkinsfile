pipeline {
    agent any

    triggers {
        cron('30 4 * * *') // This will run the pipeline every day at 10:00 AM IST (4:00 AM UTC)
    }

    environment {
        CUSTOM_PYTHON_PATH = 'C:\\Users\\Mujeeb Rahaman\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    // Create a virtual environment
                    bat "\"${CUSTOM_PYTHON_PATH}\" -m venv env"

                    // Activate the virtual environment
                    bat "call env\\Scripts\\activate.bat"

                    // Install dependencies
                    bat "\"${CUSTOM_PYTHON_PATH}\" -m pip install -r requirements.txt"

                    // Install chromedriver
                    // bat "sbase install chromedriver latest"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run pytest with headless option
                    bat "\"${CUSTOM_PYTHON_PATH}\" -m pytest --junit-xml=report.xml"
                }
            }
        }
    }

    post {
        always {
            // Archive the test reports
            archiveArtifacts 'report.xml'
            junit 'report.xml'
        }
        success {
            // Publish JUnit test result report on successful build
            junit 'report.xml'
        }
    }
}
