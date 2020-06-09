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

# Install aws-cli
AWSCLI_VERSION=1.18.75
sudo apt install awscli
sudo apt-get install python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
rm get-pip.py
pip install awscli==${AWSCLI_VERSION} --upgrade

# Install Django
DJANGO_VERSION=3.0.7
pip install django==${DJANGO_VERSION} --upgrade

# pip freeze > requirements.txt
