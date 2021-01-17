import sqlite3 as sq
import datetime as dt

conn=sq.connect('points.db')
cursor=conn.cursor()
cmd="create table X_Y(X int,Y int);
create table maintable(DATE date,TIME time);"
cursor.execute(cmd)
conn.commit()
