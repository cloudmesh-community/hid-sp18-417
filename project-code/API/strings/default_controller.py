import connexion
import six
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util


def add_string_str_get(str):  # noqa: E501
    """add_string_str_get

     # noqa: E501

    :param str: String to be added
    :type str: str

    :rtype: OUTPUT
    """
    with open('data/data.csv') as f:
        reader = csv.reader(f)
        rowCount = len(list(reader))

    with open('data/data.csv', 'a') as csvfile:
       writer = csv.writer(csvfile)
       writer.writerow([rowCount, str])
    rowList = []
    with open('data/data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            rowList.append(row) 
    
    return rowList


def fetch_string_id_get(id):  # noqa: E501
    """fetch_string_id_get

     # noqa: E501

    :param id: id for which string to be retreived
    :type id: str

    :rtype: OUTPUT
    """
    df = pd.read_csv('TSLA.csv', parse_dates = True, index_col=0)
    df.plot()
    plt.show()
    with open('data/data.csv', 'r') as the_file:
        reader = csv.reader(the_file)
        line = next((x for i, x in enumerate(reader) if i == int(id)), None)
    if line :
        return line
    else :
        return 405
