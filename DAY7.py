# import mysql.connector as sqlcon

import mysql.connector as sqlcon

db = sqlcon.connect(host = "localhost", user = "shashvat", passwd = "system", database = 'essentials')

cur = db.cursor()

cur.execute("update student set mark = 50 where sname = 'Shashvat'")
cur.execute("select * from student")

for i in cur:
	print(i)

cur.close()
db.commit()



# SQL Statements

'''

create database essentials;
drop database essentials;

show databases;
use essentials;
show tables;
create table student(roll int, sname varchar(30), mark int);
desc student;

insert into student values(1001, 'Shashvat', 30);
insert into student values(1002, 'Arun', 40);

select * from student;

update student set mark = 87 where sname = 'Varun';

set SQL_SAFE_UPDATES = 1;

drop table student;

'''