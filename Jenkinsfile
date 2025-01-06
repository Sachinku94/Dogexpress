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
                    // Run the tests inside the Docker container using docker run
                    bat "docker run --rm ${DOCKER_IMAGE} python -m pytest --alluredir=allure-results"
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Generate the Allure report using the Jenkins plugin
                    allure([
                        results: [[path: 'allure-results']],
                        reportBuildPolicy: 'ALWAYS'
                    ])
                }
            }
        }
    }

    post {
        always {
            steps {
                // Archive test results
                archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true

                // Publish Allure report
                allure([
                    results: [[path: 'allure-results']],
                    reportBuildPolicy: 'ALWAYS'
                ])
            }
        }
    }
}
