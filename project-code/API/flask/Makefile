docker-build:
	docker build -t cloudmesh/stocks .
	
docker-start:
	docker run -p 5000:5000 cloudmesh/stocks
	
docker-start-detach-mode:
	docker run -d -p 5000:5000 cloudmesh/stocks

docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

start:
	#creates the swagger service from the yaml file and places the controllers in the appropriate directory
	sudo python app/main.py
