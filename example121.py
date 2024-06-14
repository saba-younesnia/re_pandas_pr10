import pandas as pd
import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='IthinkIgotit**01',
    database='dbtest'
)
mycursor=db.cursor()

data=pd.read_csv('C:\\Users\\YOONES-NIA\\Desktop\\csv_files\\Car.csv')

l_cars=list(set(data['Car']))

ave_v=data.groupby('Car')['Volume'].mean()
l_ave_v=ave_v.tolist()

ave_co2=data.groupby('Car')['CO2'].mean()
l_ave_co2=ave_co2.tolist()

for i in range(0,len(l_cars),1):
    query = "insert into car_co2(car_name,ave_volume,ave_co2) values('" +str(l_cars[i])+"','" +str(l_ave_v[i])+"','" +str(l_ave_co2[i])+"');"
    mycursor.execute(query)
db.commit()