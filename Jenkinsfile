@Library("security_stages") _
 
pipeline {
  agent any
  
  options {
    buildDiscarder(logRotator(numToKeepStr: "3", artifactNumToKeepStr: "3"))
  }

  stages {
  //   stage('Define host for deployment') {
  //     steps {
  //       script { 
  //         properties([
  //           parameters([
  //             string(
  //               defaultValue: '', 
  //               description: "What is the IP address of the PI you which to deploy to?"
  //               name: 'IP', 
  //               trim: true
  //             )
  //           ])
  //         ])
  //       }
  //     }
  //   }

    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          python3 -m venv ./venv
          pip install -r requirements.txt
          """
        }
      }
    }
    // stage('Unit Testing') { // Perform unit testing
    //   steps {
    //     script {
    //       sh """
    //       python -m unittest discover -s tests/unit
    //       """
    //     }
    //   }
    // }

    stage ("Attempting security stages") {
      steps {
        shared()
      }
    }

    // stage("Attempting deployment") {
    //   steps {
    //     sh("""
    //       grep -qxF 'ssh-keyscan ${params.IP}' ~/.ssh/known_hosts || ssh-keyscan  ${params.IP} >> ~/.ssh/known_hosts
    //       scp your_path_to_the_file/the_file pi@${params.IP}:~/
    //     """) 
    //   }
    // }
  }
}