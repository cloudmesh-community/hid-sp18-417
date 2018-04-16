SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=string_init.yaml
DATA=data
DESTDIR=server/
FLASKDIR=server/string/flaskConnexion
all: service start 
	@echo "DONE"

container: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	sudo docker build -t cloudmesh-strings .
	@echo "image DONE"

docker-pull:
	@echo "pulling the image from dockerhub..."
	docker pull cloudmesh-strings
	@echo "image DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -p 8080:8080 cloudmesh-strings

docker-stop:
	@echo "stoping the service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image..."
	docker rmi -f cloudmesh-strings
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

dest:
	mkdir $(DESTDIR)

service:dest 
	sudo wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate  -i $(YAML)  -l python-flask  -o $(FLASKDIR)  -D supportPython2=true
	rm *.jar
	mkdir $(DATA)
	touch $(DATA)/data.csv
	cp -r data $(FLASKDIR)
	cp -r default_controller.py $(FLASKDIR)/swagger_server/controllers
	cd $(FLASKDIR) && pip install -r requirements.txt && \
	python setup.py install && python -m swagger_server	

test:
	curl http://127.0.0.1:8080/cloudmesh/strings/addString/adding-a-new-string0
	curl http://127.0.0.1:8080/cloudmesh/strings/addString/adding-a-new-string1
	curl http://127.0.0.1:8080/cloudmesh/strings/addString/adding-a-new-string2
	curl http://127.0.0.1:8080/cloudmesh/strings/addString/adding-a-new-string3
	curl http://127.0.0.1:8080/cloudmesh/strings/addString/adding-a-new-string4
	curl http://127.0.0.1:8080/cloudmesh/strings/fetchString/3
	            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	sudo rm -r $(DESTDIR)
	sudo rm -r $(DATA)

container:
	sudo docker build -t cloudmesh-strings .
	sudo docker run -p 8080:8080 cloudmesh-strings 

osx:
	docker build -t cloudmesh-strings .
	docker run -p 8080:8080 cloudmesh-strings 
