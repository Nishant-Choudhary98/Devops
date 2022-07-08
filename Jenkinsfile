pipeline {
    agent any //{ docker { image 'python:3.9.13' } }
    stages {
        stage('build') {
            steps {
                set +e
                bat 'python CSV_using_Request.py'
                set +e
            }
        }
     }
   }
