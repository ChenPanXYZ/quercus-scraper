
This tutorial is based on the assumption that the reader is using a Ubuntu 20.04 LTS system. For other systems such as Windows, Mac, some commands may need modification.

## Install Chrome (Or Firefox)

wget [https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb](https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb)

sudo dpkg -i google-chrome-stable_current_amd64.deb

sudo apt update

sudo apt upgrade

sudo apt --fix-broken install

google-chrome --version

## Install Chrome Driver

mkdir quercus-script

cd quercus-script

wget [https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip](https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip)

unzip chromedriver*.zip

## Make a virtual environment

sudo apt install python3-virtualenv

virtualenv .venv

source .venv/bin/activate

  

## Password

nano .env

## Install the dependencies

pip3 install pandas

pip3 install selenium

pip3 install python-dotenv

pip3 install lxml

pip3 install openpyxl
