pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',url: 'https://github.com/CT2-DEVOPS-Team2/myinsuranceapp.git' 
                bat 'dir'
	        }
        }        
        stage('Compile') {
            steps {
                dir ('standalone'){
                    echo 'Building...'
                    bat 'dir'
                    
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging...'                
            }
        }
        stage('Acceptance test') {
            steps {
                echo 'Acceptance...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
