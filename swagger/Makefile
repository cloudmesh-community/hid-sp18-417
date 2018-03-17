SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=string_init.yaml
DATA=data
DESTDIR=swagger_sp18_417
CONFIGDIR=~/.cloudmesh/
FLASKDIR=swagger_sp18_417/server/string/flaskConnexion

dest:
	mkdir $(DESTDIR)

service: 
	java -jar swagger-codegen-cli-2.3.1.jar generate  -i string_init.yaml  -l python-flask  -o $(FLASKDIR)  -D supportPython2=true
	cp -r data $(FLASKDIR)
	cp -r default_controller.py $(FLASKDIR)/swagger_server/controllers

run: 
	cd $(FLASKDIR) && pip install -r requirements.txt && \
	sudo python setup.py install && python -m swagger_server

test:
	            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -r $(DESTDIR)
