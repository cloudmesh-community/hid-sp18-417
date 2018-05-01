build-deploy-all: docker-build deploy-web-ui
docker-build:
	docker build -t rashray/stocks .
	
docker-start:
	docker run -p 5000:5000 rashray/stocks

docker-clean:
	docker stop $$(docker ps -a -q -f status=running)
	docker rm $(docker ps -a -q)
	docker rmi rashray/stocks

start:
	#creates the swagger service from the yaml file and places the controllers in the appropriate directory
	sudo python app/main.py

deploy-web-ui:
	docker-compose up -d
	kubectl apply -f kubernetes/flask-web-ui.yml