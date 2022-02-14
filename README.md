# api-flask

#to create a docker image

$ docker build -t apicase .

#to run the docker container

$ docker run -d -p 5000:5000 apicase

curl localhost:5000

curl localhost:5000/temperature&city="city-name"
