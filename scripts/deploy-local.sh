#!/usr/bin/env bash

# Initialize
sudo apt -y update
sudo apt -y upgrade

# Local Virtual Environment
PYTHON_VERSION=3.8.3
LOCAL_VIRTUAL_ENV_NAME="django-rest-framework-boilerplate-${PYTHON_VERSION}"
pyenv install ${PYTHON_VERSION}
pyenv virtualenv ${PYTHON_VERSION} ${LOCAL_VIRTUAL_ENV_NAME}
pyenv local ${LOCAL_VIRTUAL_ENV_NAME}

# Install Docker
sudo apt install curl
sudo apt -y install apt-transport-https ca-certificates curl
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt -y update
sudo apt -y install docker-ce
sudo usermod -aG docker "$(whoami)"
# sudo reboot

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# install requirements
pip install -U -r ./project/requirements/requirements-base.txt
