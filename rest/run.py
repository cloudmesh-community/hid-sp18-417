"""                                                          
# A program to run the rest service to get sys info using eve
# Date: 02/04/2018                                           
# Author: Rashmi Ray                                         
                                                             
"""                                                          
                                                             
from eve import Eve                                          
                                                             
import platform                                              
                                                             
app = Eve()                                                  
                                                             
#Network Name                                                
@app.route('/mysys/sys-name')                                
def sysName():                                               
     name = platform.node()                                  
     return name                                             
                                                             
@app.route('/mysys/os-name')                                 
def osName():                                                
        name = platform.system()                             
        return name                                          
                                                             
@app.route('/mysys/processor-name')                          
def processorName():                                         
         name = platform.processor()                         
         return name                                         
                                                             
if __name__ == '__main__':                                   
        app.run()                                            
