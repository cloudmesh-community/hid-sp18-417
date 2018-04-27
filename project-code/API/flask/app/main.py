from flask import Flask, render_template
import csv
import quandl as qd
import pygal as pg
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def index():
    try :
        qd.ApiConfig.api_key = "[access code]"
        mydata = qd.get_table('WIKI/PRICES', ticker = ['AAPL'])
        mydata = mydata[:2000]
        line_chart = pg.Line()
        line_chart.title = 'Stocks Analysis for AAPL'
        line_chart.add('high', mydata["high"])
        line_chart.add('low',   mydata["low"])
        line_chart.add('close', mydata["close"])
        chart = line_chart.render_data_uri()
        return render_template('index.html', graph_data=chart)
    except Exception, e:
        return str(e)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port=int(os.getenv('PORT', '5000')))
