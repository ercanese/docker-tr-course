FROM ubuntu:latest

RUN apt update && apt install vim -y
RUN apt-get install -y wget apt-transport-https software-properties-common
SHELL [ "/bin/bash","-c","source /etc/os-release" ]
RUN wget -q https://packages.microsoft.com/config/ubuntu/$VERSION_ID/packages-microsoft-prod.deb 
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get update
RUN apt-get install -y powershell


WORKDIR /app

COPY . .

CMD ["pwsh","time.ps1"]




