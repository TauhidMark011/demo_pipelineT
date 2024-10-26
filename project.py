import mysql.connector
import pandas as pd
print("modules imported")
#making a connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '1438011@Alex',
    database='trendytech'
)
cursor = conn.cursor()
print("connection got created")
cursor.execute("select * from employee;")
print("data got retrieved")
data = cursor.fetchall()
df = pd.DataFrame(data)
print(data)