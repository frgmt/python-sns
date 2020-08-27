#!/bin/bash

sudo apt update
sudo apt -f install -y
sudo apt-get install -y libappindicator3-1 xdg-utils fonts-liberation
sudo apt-get install rpm yum
sudo yum install -y vlgothic-fonts
sudo apt --fix-broken install -y

# chrome
curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
curl -O https://chromedriver.storage.googleapis.com/77.0.3865.10/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

# pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

sed -i -e 's/alias python/#alias python/g' ~/.bashrc
cat << 'EOF' >> ~/.bashrc
export PYENV_ROOT=${HOME}/.pyenv
export PATH=$PATH:$PYENV_ROOT/bin
eval "$(pyenv init -)"
EOF
source ~/.bashrc

pyenv install 3.7.3
pyenv global 3.7.3
python --version

# modules
pip install --upgrade pip
pip install -r requirements.txt

sudo ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

cd ~/environment