pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dogexpress_tests:latest" // Name of the Docker image
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git
                git branch: 'main', url: 'https://github.com/Sachinku94/Dogexpress.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the Docker container and execute tests
                    bat "docker run --rm ${DOCKER_IMAGE} python -m pytest"
                }
            }
        }
    }

    post {
        always {
            steps {
                // Archive test results
                archiveArtifacts artifacts: 'pytest-results/**', allowEmptyArchive: true
            }
        }
    }
}
