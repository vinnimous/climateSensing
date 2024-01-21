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