
MyPythonStarter
===============

Template básico para iniciar um demo em python com flask

## Requisitos

```
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install python python-pip
sudo apt-get install docker.io
export LC_ALL=C
sudo pip install -r requirements.txt
```

## Para testar 
```
python main.py
```

## Para gerar o container
```
sudo docker build -t [docker_user/app_name] --no-cache .
```

## Para publicar no docker registry
```
sudo docker login -u [user] -p [senha] -e [email]
sudo docker push [docker_user/app_name]
```
