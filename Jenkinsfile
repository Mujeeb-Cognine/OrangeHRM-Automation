pipeline {
    agent any

    environment {
        CUSTOM_PYTHON_PATH = 'C:\\Users\\Mujeeb Rahaman\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        CHROMEDRIVER_VERSION = 'latest'
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

                    // Download and install chromedriver
                    def chromedriverUrl = "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_win32.zip"
                    bat "powershell -Command Invoke-WebRequest -Uri ${chromedriverUrl} -OutFile chromedriver.zip"
                    bat "powershell -Command Expand-Archive -Path chromedriver.zip -DestinationPath ."

                    // Add chromedriver to PATH
                    bat "setx PATH \"%PATH%;${env.WORKSPACE}\\chromedriver.exe\""
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run pytest with headless option
                    bat "\"${CUSTOM_PYTHON_PATH}\" -m pytest --junit-xml=report.xml --headless"
                }
            }
        }
    }

    post {
        always {
            // Archive the test reports
            archiveArtifacts 'report.xml'
        }
    }
}
