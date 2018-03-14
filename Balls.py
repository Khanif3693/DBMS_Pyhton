import csv
import MySQLdb

print("Enter  File  To Be Export")
conn = MySQLdb.connect("localhost","root","Unknown","pytb" )
cursor = conn.cursor()
#sql = 'CREATE DATABASE test1'
sql ='''DROP TABLE IF EXISTS `BALLS`; CREATE TABLE BALLS (PID INT NOT NULL PRIMARY KEY,PLAYER VARCHAR(50) ,SPAN VARCHAR(20),MAT VARCHAR(20), INNINGS INT,BALLS DOUBLE,RUNS DOUBLE,WICKETS DOUBLE, BBM VARCHAR(20), AVG DOUBLE, ECONOMY DOUBLE, SR DOUBLE,FIVE_WICKETS INT, TEN_WICKETS INT,CATCHES INT,STUMP INT,COUNTRY VARCHAR(50),FORMAT VARCHAR(20) )'''
cursor.execute(sql)

with open('Ball.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['PID'],row['Player'],row['Span'],row['Mat'],row['Inns'], row['Balls'],row['Runs'],row['Wkts'], row['Bbm'], row['Ave'], row['Econ'],row['Sr'],row['5s'],row['10s'],row['Ct'],row['St'],row['Country'],row['Format'])
        # insert
        conn = MySQLdb.connect("localhost","root","Unknown","pytb" )
        sql_statement = "INSERT INTO BALLS(PID,PLAYER ,SPAN ,MAT , INNINGS,BALLS ,RUNS ,WICKETS , BBM, AVG , ECONOMY,SR,FIVE_WICKETS , TEN_WICKETS ,CATCHES, STUMP ,COUNTRY ,FORMAT ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement,[(row['PID'],row['Player'],row['Span'],row['Mat'],row['Inns'], row['Balls'],row['Runs'],row['Wkts'], row['Bbm'], row['Ave'], row['Econ'],row['Sr'],row['5s'],row['10s'],row['Ct'],row['St'],row['Country'],row['Format'])])
        conn.escape_string(sql_statement)
        conn.commit()
