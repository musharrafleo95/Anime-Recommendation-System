pipeline{
    agent any

    stages {
        // stages start
        stage("Cloning from Github......"){
            steps{
                script{
                    echo "Cloning from Github.."
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '4636e257-29a8-470f-b72c-1cb46126a58f', url: 'https://github.com/musharrafleo95/Anime-Recommendation-System.git']])
                }
            }
        }
    
    
    
    
    
    
    
    
    
    // stages end
    }
}