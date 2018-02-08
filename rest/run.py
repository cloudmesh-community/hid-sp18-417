from eve import Eve
import platform
import json
import psutil
from flask import jsonify

app = Eve()

#Network Name
@app.route('/sys-name')
def sysName():
     name = platform.node()
     return name

@app.route('/os-name')
def osName():
        name = platform.system()
        return name

@app.route('/processor-name')
def processorName():
         name = platform.processor()
         return name

@app.route('/disk-info')
def getDiskInfo():
         diskData = jsonify(psutil.disk_usage('/'))
         return diskData

@app.route('/all-info')
def getAllInfo():
        all_info = {
                "diskData": {
                        "disk-total": psutil.disk_usage('/').total,
                        "disk-used": psutil.disk_usage('/').used,
                        "disk-free": psutil.disk_usage('/').free,
                        "disk-percent": psutil.disk_usage('/').percent
                },
                "systemData": {
                         "machine": platform.machine(),
                         "name": platform.node(),
                         "processor": platform.processor(),
                         "OS": platform.system(),
                         "version": platform.version()
                }
        }
        json_disk = (all_info)
        response = app.response_class(
                 response=json.dumps(all_info,sort_keys=True,indent=4),
                 status=200,
                 mimetype='application/json'
             )
        return response


if __name__ == '__main__':
        app.run()
