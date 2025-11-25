#!/bin/bash
sudo apt-get update && sudo apt-get install -y openjdk-17-jdk wget unzip
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-25.11.0.114957.zip
unzip sonarqube-25.11.0.114957.zip
sudo mv sonarqube-25.11.0.114957 /opt/sonarqube
sudo useradd sonar
sudo chown -R sonar:sonar /opt/sonarqube
sudo -u sonar /opt/sonarqube/bin/linux-x86-64/sonar.sh start
