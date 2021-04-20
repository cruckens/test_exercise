def retrigger() { 
  sleep 30
  cleanWs()
  build (job: JOB_BASE_NAME, wait: false, propagate:false)
}

pipeline {
  agent any
  options { disableConcurrentBuilds() }
  parameters {
    choice(choices: 'Tel Aviv', description: 'City to get the weather for', name: 'city')
  }
  stages {
    stage ('Python hello') {
      steps {
        script {
          withCredentials([string(credentialsId: 'app_id', variable: 'api_key')]) {
            withEnv(["PYTHONPATH=${env.WORKSPACE}/dependencies"]) {
                sh 'python hello.py --city "$city" --appid $api_key'
            }
          }
        }
      }
    }
  }
  post {
    always {
      retrigger()
    }
  }
}