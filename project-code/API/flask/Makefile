docker-build:
	docker build -t rashray/flask .
	
docker-start:
	docker run -p 8080:8080 rashray/flask
	
docker-start-detach-mode:
	docker run -d -p 8080:8080 rashray/flask

docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

service:
	#creates the swagger service from the yaml file and places the controllers in the appropriate directory
	sudo python app.py
