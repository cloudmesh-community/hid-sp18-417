from flask import Flask, render_template
import csv
import quandl as qd
import pygal as pg
import pandas as pd
import os
from flask import request
import datetime

app = Flask(__name__)
@app.route("/home")
def index():
    try :
        initialTime=datetime.datetime.now()
        companycode = request.args.get('code')
        qd.ApiConfig.api_key = "oysPL-gX3EsUsTSPzeib"
        completeData = qd.get_table('WIKI/PRICES', ticker = [companycode])
        ##completeData.to_csv(companycode+'.csv')
        mydata = completeData[:2000]
        line_chart = pg.Line()
        line_chart.title = 'Stocks Analysis for ' + companycode
        line_chart.add('high', mydata["high"])
        line_chart.add('low',   mydata["low"])
        line_chart.add('close', mydata["close"])
        chart = line_chart.render_data_uri()
        loadTime=datetime.datetime.now()
        return render_template('index.html', graph_data=chart, companycode=companycode, initialTime=initialTime,loadTime=loadTime)
    except Exception, e:
        return str(e)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False, port=int(os.getenv('PORT', '5000')))
