## Swagger Rest API Assignment
This swagger API exploits CSV[/data/data.csv] to store and retrieve string data.
 
 ### Specification:
 String_init.yaml
 string.yaml[to be integrated]
 
 ### Setup:
 * gitclone the codebase
 * change directory to swagger_assignment/server/string/flaskConnexion [ cd .../swagger_assignment/server/string/flaskConnexion]
 * Now install the requirements [pip install -r requirements.txt]
 * run setup.py [ python setup.py install]
 * finally run the server [python -m swagger_server]
 * now the needed end points can be used to consume the service
 
 ### End-points:
 #### basepath is /v2
 * /addString/{str} : This method will add the string from the query param to the data collection. and display the current collection of rows in the CSV.
  ``` 
  http://localhost:8080/v2/addString/String to added here
 
  #### Output:
  [{
  1,string
  },
  {
  2, row 2
  ...}]
   ```

* /fetchString/{id} : This method fetch the string by id and displays the row
  ``` 
  http://localhost:8080/v2/addString/2
  #### Output:
  {
  2, row 2
  }
   ``` 
### Error Handling:
to do
