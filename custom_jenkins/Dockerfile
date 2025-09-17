# Use the Jenkins image as the base image
FROM jenkins/jenkins:lts

# Switch to root user to install dependencies
USER root

# Install prerequisites and Docker
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean

# Installing python3 and changing its name to python in the system
RUN apt install -y python3 && \
    python3 --version && \
    ln -s /usr/bin/python3 /usr/bin/python  && \
    python --version && \
    apt install -y python3-pip && \
    apt install -y python3-venv

# INSTALL GOOGLE CLOUD  and Kubernetes CLI ON JENKINS CONTAINER
RUN apt-get install -y curl apt-transport-https ca-certificates gnupg && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    apt-get update && apt-get install -y google-cloud-sdk && \
    apt-get update && apt-get install -y kubectl && \
    apt-get install -y google-cloud-sdk-gke-gcloud-auth-plugin && \
    kubectl version --client && \
    gcloud --version

# Add Jenkins user to the Docker group (create if it doesn't exist)
RUN groupadd -f docker && \
    usermod -aG docker jenkins && \
    usermod -aG root jenkins && \

# Create the Docker directory and volume for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Switch back to the Jenkins user
USER jenkins