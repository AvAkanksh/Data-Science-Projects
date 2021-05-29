import string
import matplotlib.pyplot as plt
import pandas as pd


def avg_data_2013():
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize=24):
        avg = rows[rows['PM2.5'].apply(lambda x : str(x)[0] in string.digits )]['PM2.5'].apply(float).mean()
        average.append(avg)
    return average

    
def avg_data_2014():
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize=24):
        avg = rows[rows['PM2.5'].apply(lambda x : str(x)[0] in string.digits )]['PM2.5'].apply(float).mean()
        average.append(avg)
    return average


def avg_data_2015():
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize=24):
        avg = rows[rows['PM2.5'].apply(lambda x : str(x)[0] in string.digits )]['PM2.5'].apply(float).mean()
        average.append(avg)
    return average


def avg_data_2016():
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize=24):
        avg = rows[rows['PM2.5'].apply(lambda x : str(x)[0] in string.digits )]['PM2.5'].apply(float).mean()
        average.append(avg)
    return average

 
def avg_data_2017():
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize=24):
        avg = rows[rows['PM2.5'].apply(lambda x : str(x)[0] in string.digits )]['PM2.5'].apply(float).mean()
        average.append(avg)
    return average

    
def avg_data_2018():
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize=24):
        avg = rows[rows['PM2.5'].apply(lambda x : str(x)[0] in string.digits )]['PM2.5'].apply(float).mean()
        average.append(avg)
    return average


if __name__=="__main__":
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.plot(range(0,365),lst2015,label="2015 data")
    plt.plot(range(0,365),lst2016,label="2016 data")
    plt.plot(range(0,365),lst2017,label="2017 data")
    plt.plot(range(0,364),lst2018,label="2018 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc=0)
    plt.show()
