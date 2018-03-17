SWAGGERCODEGEN=java -jar swagger-codegen-cli.jar
YAMLFILE=string.yaml
DATA=data
DESTDIR=server/
CONFIGDIR=~/.cloudmesh/
FLASKDIR=flaskConnexion/

dest:
	mkdir swagger_sp18_417

service: 
	java -jar swagger-codegen-cli-2.3.1.jar generate  -i string_init.yaml  -l python-flask  -o swagger_sp18_417/server/string/flaskConnexion  -D supportPython2=true
	cp -r data swagger_sp18_417/server/string/flaskConnexion
	cp -r default_controller.py swagger_sp18_417/server/string/flaskConnexion/swagger_server/controllers

run: 
	cd swagger_sp18_417/server/string/flaskConnexion && pip install -r requirements.txt && \
	sudo python setup.py install && python -m swagger_server

test:
	            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -r $(DESTDIR)
	rm -r $(CONFIGDIR)
