pipeline {
    agent any //{ docker { image 'python:3.9.13' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 CSV_using_Request.py'
            }
        }
     }
   }
