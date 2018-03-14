import csv
import MySQLdb

print("Enter  File  To Be Export")
conn = MySQLdb.connect("localhost","root","******","pytb" )
cursor = conn.cursor()
#sql = 'CREATE DATABASE test1'
sql ='''DROP TABLE IF EXISTS `BATS`; CREATE TABLE BATS (PID INT NOT NULL,PLAYER  VARCHAR(50) NOT NULL,SPAN VARCHAR(20),MAT VARCHAR(20), INNINGS INT,NOT_OUT INT,RUNS DOUBLE,HS VARCHAR(20),AVG FLOAT(20), TONS INT, FIFTY INT, DUCKS INT, COUNTRY VARCHAR(20),FORMAT VARCHAR(20),PRIMARY KEY(PID) )'''
cursor.execute(sql)

with open('Bat.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['PID'],row['Player'],row['Span'],row['Mat'],row['Inns'], row['No'],row['Runs'],row['Hs'], row['Ave'], row['100'], row['50'],row['Ducks'],
	row['Country'],row['Format'])
        # insert
        conn = MySQLdb.connect("localhost","root","******","pytb" )
        sql_statement = "INSERT INTO BATS(PID,PLAYER ,SPAN,MAT , INNINGS ,NOT_OUT ,RUNS , HS ,AVG, TONS, FIFTY , DUCKS, COUNTRY,FORMAT) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement,[(row['PID'],row['Player'], row['Span'],row['Mat'], row['Inns'], row['No'],row['Runs'],row['Hs'], row['Ave'], row['100'], row['50'],row['Ducks'],row['Country'],row['Format'])])
        conn.escape_string(sql_statement)
        conn.commit()
