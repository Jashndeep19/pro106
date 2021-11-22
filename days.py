import plotly_express as px
import csv
import numpy as np

with open ("days-marks.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig=px.scatter(df,x="Marks",y="Days")
    fig.show()
    
def getDataSource (data_path):
    total_marks=[]
    days_present=[]
    with open (data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            total_marks.append(float(row["Marks"]))
            days_present.append(float(row["Days"]))

    return{"x":total_marks,"y":days_present}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between temprature and ice cream sales:\n-->",correlation[0,1])

def setup():
    data_path = "days-marks.csv" 

    datasource = getDataSource(data_path) 
    findCorrelation(datasource) 
   # plotFigure(data_path) 

setup()