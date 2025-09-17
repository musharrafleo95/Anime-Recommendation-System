pipeline{
    agent any

    environment {
        VENV_DIR = ".venv"
        GCP_PROJECT = 'mlops-471718'
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
        KUBECTL_AUTH_PLUGIN = "/usr/lib/google-cloud-sdk/bin"
    }

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
        // stage start
        stage("Making virtual environment in Jenkins container......"){
            steps{
                script{
                    echo "Making virtual environment in container managed by jenkins......"
                    sh'''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install dvc
                    '''

                }
            }
        }
    
        // stage start
        stage("DVC pull"){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script{
                        echo 'DVC Pull.....'
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        dvc pull
                        '''
                    }
                }
            }
        }
        // // stage start
        // stage("Build and Push Image to GCR"){
        //     steps{
        //         withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
        //             script{
        //                 echo 'Build and Push Image to GCR.....'
        //                 sh '''
        //                 . ${VENV_DIR}/bin/activate
        //                 dvc pull
        //                 '''
        //             }
        //         }
        //     }
        // }
    
    
    
    
    
    
    
    
    // stages end
    }
}