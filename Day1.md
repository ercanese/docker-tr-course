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



