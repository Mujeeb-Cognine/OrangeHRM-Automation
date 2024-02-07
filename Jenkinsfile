pipeline {
    agent any

    environment {
        CUSTOM_PYTHON_PATH = 'C:\\path\\to\\your\\custom\\python.exe'
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

                    // Download chromedriver from a mirror using TLS 1.2
                    def chromedriverUrl = "https://npm.taobao.org/mirrors/chromedriver/${CHROMEDRIVER_VERSION}/chromedriver_win32.zip"
                    def downloadCommand = "powershell -Command [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri ${chromedriverUrl} -OutFile chromedriver.zip"
                    bat downloadCommand
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
