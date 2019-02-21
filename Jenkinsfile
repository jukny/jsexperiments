pipeline {
  agent any
  stages {
    stage('One') {
      parallel {
        stage('One') {
          steps {
            sh 'echo "Hello world!"'
            pwd(tmp: true)
          }
        }
        stage('One-1') {
          steps {
            sh 'echo "Hello again"'
          }
        }
      }
    }
    stage('Two') {
      steps {
        sh 'echo $FOO'
      }
    }
  }
  environment {
    Foo = '1234'
  }
}