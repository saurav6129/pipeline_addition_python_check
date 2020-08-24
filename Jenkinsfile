pipeline {
    agent none
    stages {
        stage('Python build') {
			agent {
				docker {
					image 'python:2-alpine'
				}
			}
			
            steps {
                sh 'python --version'
				sh 'python -m py_compile sources/calulator.py'
				echo'testing build trigger. '
				echo'again testing build trigger in automation.'
				echo'again checking.'
            }
        }
    
		stage('Python test') {
			agent {
				docker {
					image 'qnib/pytest'
				
				}
			}
			
			steps {
				sh'py.test -v sources/test_func.py'
				echo'testing finished.'
			
			}
		}
	}
}