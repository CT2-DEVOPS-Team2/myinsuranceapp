pipeline {
    agent {label "linux"}
	options {
		buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', days
ToKeepStr: '', num ToKeepStr: '5')
	disableConcurrentBuilds()
}
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}

