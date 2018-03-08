SWAGGERCODEGEN=java -jar swagger-codegen-cli.jar
YAMLFILE=string.yaml
DATA=data
DESTDIR=server/
CONFIGDIR=~/.cloudmesh/
FLASKDIR=flaskConnexion/

dest:
	mkdir $(DESTDIR)
	mkdir $(CONFIGDIR)

service: dest
	$(SWAGGERCODEGEN) generate -i $(YAMLFILE) -l python-flask -o $(DESTDIR) -D supportPython2=true
	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cp -r $(DATA) $(FLASKDIR)

run: 
	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install && python -m swagger_server

test:
	            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -r $(DESTDIR)
	rm -r $(CONFIGDIR)
