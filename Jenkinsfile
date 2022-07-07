pipeline {
    agent { docker { image 'python:3.9.13' } }
    stages {
        stage('build') {
            steps {
                powershell 'python CSV_using_Request.py'
            }
        }
     }
   }
