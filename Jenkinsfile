pipeline {
    agent any

    stages {
        stage('Pull Code from SCM') {
            steps {
                 script{
                 if(fileExists("$WORKSPACE/demo_project/.git")){
                    dir("$WORKSPACE/demo_project/"){
                    sh 'git pull'
                    }
                    }
                 else{
                    sh 'git clone https://github.com/akshayinamdarbjp/demo_project.git'
                    }
                }
            
            }
            }
        stage('Build the docker image') {
            steps {
                script {
                   sh 'docker build --tag flask-docker-demo-app $WORKSPACE/demo_project/'
                }
            }
        }
        stage('Docker Run') {
            steps {
              sh' docker stop flask-docker-demo-app'
              sh' docker rm flask-docker-demo-app'
              sh' docker run --name flask-docker-demo-app -d -p 80:80 flask-docker-demo-app'
            }
        }
        stage('Test the output') {
            steps {
                script {
                    ReturnedOutput = sh(script: 'curl -s -XGET "http://127.0.0.1:80"', returnStdout: true)
                    ExpectedOuput = '"Hello Airbus"'
                    echo "Build full flag: ${ReturnedOutput}"
                    echo "Build full flag: ${ExpectedOuput}"
                    if (ReturnedOutput==ExpectedOuput){
                      echo "Build full flag: Result is expected"
                    }else{
                      echo "Build full flag: Result is not expected"
                    }
                }
            }
        }
    }
}

