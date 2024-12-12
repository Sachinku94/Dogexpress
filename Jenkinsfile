pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dogexpress_tests:latest" // Name for the Docker image
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git
                git branch: 'main', url: 'https://github.com/Sachinku94/Dogexpress.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                # Install required Python dependencies
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image for the test environment
                    docker.build(env.DOCKER_IMAGE)
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the Docker image and execute tests
                    docker.image(env.DOCKER_IMAGE).inside {
                        sh 'pytest --alluredir=allure-results'
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
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
