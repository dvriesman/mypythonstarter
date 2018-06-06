
MyPythonStarter
===============

Template básico para iniciar um demo em python com flask

##Requisitos

```
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install python python-pip
sudo apt-get install docker.io
```

##Para testar 
python main.py

##Para gerar o container
docker build -t [docker_user/app_name] --no-cache .

##Para publicar no docker registry
docker login -u [user] -p [senha] -e [email]
docker push [docker_user/app_name]
