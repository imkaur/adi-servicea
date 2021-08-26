pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = "mandeep1690/servicea"
 	dockerfile= "Dockerfile"   
}
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation'
            }
        }
	 stage('Initialize'){
     		def dockerHome = tool 'myDocker'
		env.PATH = "${dockerHome}/bin:${env.PATH}"
    	}
        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                script {
		    app = docker.build(DOCKER_IMAGE_NAME, "-f serviceA/${dockerfile} .")
                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockercred') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('DeployToProduction') {
            when {
                branch 'main'
            }
            steps {
//                input 'Deploy to Production?'
                milestone(1)
		script {
		   sh """
			/usr/local/bin/helm upgrade --install servicea-app serviceA/helm-charts/appservicea/ --values serviceA/helm-charts/appservicea/values.yaml --set image.tag="${env.BUILD_NUMBER}" --kubeconfig  /home/cloud_user/.kube/config
		"""
		}
            }
        }
    }
}
