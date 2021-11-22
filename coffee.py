import plotly_express as px
import csv
import numpy as np

with open ("coffee-sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig=px.scatter(df,x="Coffee",y="sleep")
    fig.show()


def getDataSource (data_path):
    coffee=[]
    sleep=[]
    with open (data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["sleep"]))

    return{"x":coffee,"y":sleep}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between coffee drank and sleep is:\n-->",correlation[0,1])

def setup():
    data_path = "coffee-sleep.csv" 

    datasource = getDataSource(data_path) 
    findCorrelation(datasource) 
   # plotFigure(data_path) 

setup()