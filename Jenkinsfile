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
                    // Create and activate a virtual environment
                    def venvPath = "${WORKSPACE}/venv"
                    bat "python -m venv ${venvPath}"
                    // Activate the virtual environment and install dependencies
                    bat "${venvPath}\\Scripts\\activate && pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests and Generate HTML Report') {
            steps {
                script {
                    // Run tests with pytest and generate HTML report
                    bat "${WORKSPACE}/venv/Scripts/activate && pytest --browser_name chrome --environment default_env --html=report.html"
                }
                // Print the URL of the HTML report to the Jenkins console log
                script {
                    def buildUrl = env.BUILD_URL
                    def reportUrl = "${buildUrl}HTML_Report/"
                    echo "HTML Report URL: ${reportUrl}"
                }
                // Publish the HTML report as part of the build results
                publishHTML(target: [allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '.', reportFiles: 'report.html', reportName: 'HTML Report'])
            }
        }
    }
}
