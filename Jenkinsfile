pipeline {
  environment {
    registry = "apthailand/suchat_s"
    registryCredential = 'docker_ossuchas'
    dockerImage = ''
    image_tag_number = 'iwebvendorchatbot_api_v3.0.2'
    deployments = 'iwebvendorchatbot'
    projects = 'testrepo'
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/ossuchas/iWebVendorChatbot.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":" + image_tag_number
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Deploy to OKD') {
      steps{
          sh "oc login --insecure-skip-tls-verify https://devops01-master.apthai.com:8443 -usuchat_s -pP@ssw0rd"
          sh "oc project $projects"
          sh "oc patch dc $deployments --patch='{\"spec\":{\"template\":{\"spec\":{\"containers\":[{\"name\": \"$deployments\", \"image\":\"docker.io/$registry:$image_tag_number\"}]}}}}'"
      }
    }
  }
}
