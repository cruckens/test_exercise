def retrigger() { 
  sleep 30
  build (job: JOB_BASE_NAME, wait: false, propagate:false)
}

pipeline {
  agent any
  stages {
    stage ('Python hello') {
      steps {
        script {
          sh (script: 'python hello.py')
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