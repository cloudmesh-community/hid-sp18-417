SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=string_init.yaml
DATA=data
DESTDIR=server/string/flaskConnexion
CREATED=server
STRPDIR=string

all: service start 
	@echo "DONE"

docker-all: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker build -t rashray417/cloudmesh-strings .
	@echo "image DONE"

docker-pull:
	@echo "pulling the image from dockerhub..."
	docker pull rashray417/cloudmesh-strings
	@echo "image DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -p 8080:8080 rashray417/cloudmesh-strings


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
	mkdir -p $(DESTDIR)

service:dest 
	@echo "creating the service..."
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython3=true
	
	rm *.jar
	
	mkdir $(DATA)
	touch $(DATA)/data.csv
	cp -r data $(DESTDIR)
	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cd $(STRDIR) && pip install -r requirements.txt && python setup.py install
	
	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install 

test:
	curl http://localhost:8080/cloudmesh/strings/addString/adding-a-new-string0
	
	curl http://localhost:8080/cloudmesh/strings/addString/adding-a-new-string1
	
	curl http://localhost:8080/cloudmesh/strings/addString/adding-a-new-string2
	
	curl http://localhost:8080/cloudmesh/strings/addString/adding-a-new-string3
	
	curl http://localhost:8080/cloudmesh/strings/addString/adding-a-new-string4
	
	curl http://localhost:8080/cloudmesh/strings/fetchString/3
	            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -rf $(CREATED)

