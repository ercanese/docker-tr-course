#Docker versiyon listeleme komutu

docker version

#Bir imaj indirmek için kullandığımız komut

docker pull <imagename>
docker pull ubuntu

#Tag ile imaj indirmek için.

docker pull <imagename>:<tag>
docker pull ubuntu:22.04

#Docker login komutu kullanmadan private bir registryden eğer auth işlemi varsa imaj çekme/gönderme işlemi yapılmadan önce login komutu çalıştırılmalı.

docker login -u hroot -p dasdasd docker.tbb.com
docker logout docker.tbb.com


#Localde bulunan imajları listelemek için.
docker images


#Bir ubuntu imajından adı demo olan bir container türetin.
#İçerisine vi uygulamasını kuralım.

apt update
apt install vim
exit
docker run -it --name ubuntudemo ubuntu /bin/bash

#Tüm containerların sadece idleri listelemek için.

docker ps -qa
docker ps -a
docker ps 

#Containerları silmek için.
docker rm <containerid>

#tüm containerları silmek için
docker rm $(docker ps -qa)

#çalışan bir containeri silmek için.
docker rm <containerid> -f

#Containerlar biribirinden izole bir yapıya sahiptir.
#Container imajları read-only olarak kullanılmaktadır.


#bir containeri arka planda çalıştırmak için.
docker run -d --name <optionalname> <image>:<optag>
docker run -d --name clock2 jpettzzo/clock 

#container durdurmak için kullanılan komutlar.

docker stop <containerid> #10 saniye süreyle kapatma sinyali gönderir.
docker kill <containerid> #direk olarak containeri kill eder.

#Arka planda 3 adet clock çalışacak şekilde container oluşturalım.
#Clock1 olan containeri stop komutu ile.
#Clock2 olan containeri kill komutu ile durduralım.


#docker içerisine girmeden logları görüntülemek için kullandığımız komut.

docker logs <containerid>
docker logs -f <containerid> #çalışan containerin loglarını takip etmek için.

#imajları silmek için kullanılan komut

docker rmi <imageid>
docker rmi 1221 -f


#Container ile imaj arasındaki farkları ekranda görmek için
docker diff <containerid>
docker diff 1b52342

#Container imajlarının geçmişi ile ilgili bilgi almak için
docker history <imageid>
docker history 1ce2313


#Bir adet ubuntu imajından terminale düşecek şekilde bir container oluşturun.
#Oluşturduğunuz bu containeri güncelleyin.
#Sonrasında figlet paketini bu containera kuralım.

apt update
apt install figlet
figlet ercan ese

#Containerdan çıkalım ve imaj ile arasındaki farklara bakalım.

#tüm docker objelerinin konfigürasyonlarını görüntülemek için.
docker inspect <objectid>
docker inspect 1c2

#Inspect komutu ile formatlama işlemi yapabiliriz.

docker inspect <containersid> -f '{{ .JsonObject }}'
docker inspect <containersid> -f '{{ .JsonObject }} / {{ .JsonObject }}'

#Ekranda sadece tüm containerların ismini ve state.status değerini ekranda görelim.

docker inspect $(docker ps -qa) -f '{{ .Name }},{{ .State.Status }}'

#PowerShell uygulamasını container içerisinde çalıştırma.
docker run -it --name pwshdemo ubuntu 
apt update
apt install vim -y

apt-get install -y wget apt-transport-https software-properties-common

# Get the version of Ubuntu
source /etc/os-release

# Download the Microsoft repository keys
wget -q https://packages.microsoft.com/config/ubuntu/$VERSION_ID/packages-microsoft-prod.deb
# Register the Microsoft repository keys
dpkg -i packages-microsoft-prod.deb
# Update the list of packages after we added packages.microsoft.com
apt-get update
###################################
# Install PowerShell
apt-get install -y powershell

pwsh # PowerShell çalışıyormu kontrol et.
exit

mkdir /app
cd app/

vi Time.ps1
insert için i tuşuna bas altta insert olmalı.
shift insert tusu ile komutu yapıştır.

while($true){
    Write-Host (Get-Date)
    Start-Sleep 1
}

:wq! # çıkış

pwsh Time.ps1

ctrl-c


#bir containeri imaj haline getirmek için.
docker commit <containername> <newimagename:tag>

#Commit esnasında bir arguman değiştirmek için.

docker commit --change 'WORKDIR /app' --change 'CMD ["pwsh","time.ps1"]'


mkdir demo
cd demo
git clone https://github.com/ercanese/docker-tr-course.git

cd docker-tr-course/tbbdemo/publish

docker pull mcr.microsoft.com/dotnet/aspnet:7.0

docker run -it --name mvcdemo mcr.microsoft.com/dotnet/aspnet:7.0
mkdir app
exit

docker cp . 1231:/app

docker start -i 1231

cd /app
dotnet tbbdemo.dll

docker commit --change 'WORKDIR /app' --change 'CMD ["dotnet","tbbdemo.dll"]' mvc mvc:v1

docker run -d -p 8080:80 --name mvcapp01 mvc:v1

#Otomatik olarak build almak için Dockerfile oluşturulmalı ve aşağıdaki komut çalıştırılmalı.

docker build --tag ercan:v1 --file Dockerfile .