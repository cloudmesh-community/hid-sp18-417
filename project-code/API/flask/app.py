from flask import Flask, render_template
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import quandl as qd
import pygal as pg
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    try :
        qd.ApiConfig.api_key = "oysPL-gX3EsUsTSPzeib"
        mydata = qd.get_table('WIKI/PRICES', ticker = ['AAPL'])
        mydata = mydata[:2000]
        mydata.to_csv('test.csv')
        line_chart = pg.Line()
        line_chart.title = 'Browser usage evolution (in %)'
        line_chart.add('high', mydata["high"])
        line_chart.add('low',   mydata["low"])
        line_chart.add('close', mydata["close"])
        chart = line_chart.render_data_uri()
        return render_template('index.html', graph_data=chart)
    except Exception, e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
