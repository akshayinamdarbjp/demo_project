pipeline {
  agent any

  stages {
    stage('Pull Code from SCM') {
      steps {
        script {
          if (fileExists("$WORKSPACE/demo_project/.git")) {
            dir("$WORKSPACE/demo_project/") {
              sh 'git pull'
            }
          } else {
            sh 'git clone https://github.com/akshayinamdarbjp/demo_project.git'
          }
        }
      }
      post {
        success {
          slackSend channel: '#demo-app', color: 'good', message: 'Pull code from SCM Successful', teamDomain: 'jenkinsintegr-eaq8268', tokenCredentialId: 'SlackCred'
        }
        failure {
          slackSend channel: '#demo-app', color: 'bad', message: 'Pull code from SCM Failed', teamDomain: 'jenkinsintegr-eaq8268', tokenCredentialId: 'SlackCred'

        }
      }
    }
    stage('Build the docker image') {
      steps {
        script {
          sh 'docker build --tag demo-app $WORKSPACE/demo_project/'
        }

      }
      post {
        success {
          slackSend channel: '#demo-app', color: 'good', message: 'Docker Build was Successful', teamDomain: 'jenkinsintegr-eaq8268', tokenCredentialId: 'SlackCred'
        }
        failure {
          slackSend channel: '#demo-app', color: 'bad', message: 'Docker Build Failed', teamDomain: 'jenkinsintegr-eaq8268', tokenCredentialId: 'SlackCred'

        }
      }
    }
    stage('Docker Run') {
      steps {
        script {
          sh ' docker ps -q --filter "name=demo-app" | grep -q . && docker stop demo-app  || docker rm -fv demo-app || true'
          sh ' sleep 5'
          sh ' docker run --name demo-app -d -p 80:80 demo-app'
        }
      }
      post {
        success {
          slackSend channel: '#demo-app', color: 'good', message: 'Running Docker Container', teamDomain: 'jenkinsintegr-eaq8268', tokenCredentialId: 'SlackCred'
        }
        failure {
          slackSend channel: '#demo-app', color: 'bad', message: 'Running Docker Container Failed', teamDomain: 'jenkinsintegr-eaq8268', tokenCredentialId: 'SlackCred'

        }
      }
    }
    stage('Test the output') {
      steps {
        script {
          sleep 5
          ReturnedOutput = sh(script: 'curl -s -XGET "http://127.0.0.1:80"', returnStdout: true)
          ExpectedOutput = '"Hello Airbus"'
          echo "Build full flag: ${ReturnedOutput}"
          echo "Build full flag: ${ExpectedOutput}"
        }
      }
      post {
        success {
          slackSend channel: '#demo-app', color: 'good', message: "Curl returned the following ${ReturnedOutput}, Expected was  ${ExpectedOutput}", teamDomain: 'jenkinsintegr-eaq8268', tokenCredentialId: 'SlackCred'
        }
        failure {
          slackSend channel: '#demo-app', color: 'bad', message: "Curl failed to produce the expected results", teamDomain: 'jenkinsintegr-eaq8268', tokenCredentialId: 'SlackCred'

        }
      }
    }
  }
}
