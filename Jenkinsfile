pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dogexpress_tests:latest" // Name of the Docker image
        SELENIUM_GRID_URL = "http://selenium-grid-hub:4444/wd/hub"  // Replace with actual Selenium Grid Hub URL
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
                    // Run the Docker container and pass the Selenium Grid URL
                    bat """
                    docker run --rm -e SELENIUM_GRID_URL=${SELENIUM_GRID_URL} -v C:/ProgramData/Jenkins/.jenkins/workspace/Dogexpress:/app -w /app ${DOCKER_IMAGE} python -m pytest
                    """
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
