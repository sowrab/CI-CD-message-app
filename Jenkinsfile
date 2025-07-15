pipeline {
  agent any
  environment {
    DOCKERHUB_USER = 'sowrabhk'
    DOCKERHUB_PASS = credentials('dockerhub-creds')
  }
  stages {
    stage('Build Docker Images') {
      steps {
        sh 'docker build -t $DOCKERHUB_USER/frontend:latest ./frontend'
        sh 'docker build -t $DOCKERHUB_USER/backend:latest ./backend'
      }
    }
    stage('Push Docker Images') {
      steps {
        sh "echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin"
        sh 'docker push $DOCKERHUB_USER/frontend:latest'
        sh 'docker push $DOCKERHUB_USER/backend:latest'
      }
    }
    stage('Deploy to EC2') {
      steps {
        sshagent (credentials: ['ec2-ssh-key']) {
          sh '''
          ssh -o StrictHostKeyChecking=no ubuntu@98.81.246.162 '
            cd ~/deploy &&
            git pull origin main &&
            docker pull $DOCKERHUB_USER/frontend:latest &&
            docker pull $DOCKERHUB_USER/backend:latest &&
            docker-compose -f docker-compose.prod.yml up -d
          '
          '''
        }
      }
    }
  }
}
