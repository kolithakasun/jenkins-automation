pipeline {
    agent any
    
    environment {
        USER_CREDENTIALS = credentials('sharepoint-cred')
    }

    stages {
        stage('Checkout') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main',
                    url: 'https://github.com/kolithakasun/jenkins-automation.git'
            }
        }
        
        stage('Execute Script') {
            steps {
                sh "pip3 install -r requirement.txt"
                sh "python3 file_upload.py DasanayakeDMMK@mahamalage.com Kasun@123 $FILE_NAME"
            }
        }
    }
}
