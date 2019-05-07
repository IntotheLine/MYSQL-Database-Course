import MySQLdb as db

conn = db.connect(host='localhost', user='eguser', passwd = 'PASSWORD', databse ='egdb')
cursor = conn.cursor()

#create table
cursor.execute("""
create table server_log( log_id int not null auto_increment,
hostname varchar(32) not null,
entry_date datetime not null,
process varchar(32) not null,
detail text,
primeary key(log_id)
);
""")

#select from table
cursor.execute("Select * from server_log where process like %s", ('postfix',))
record = cursor.fetchone()
print(record)

#update row
print('updating row...')
cursor.execute('update server_log set hostname = %s where process like %s",('mcp-http', 'httpd'))

#delete row
print('deleting row...')
cursor.execute("delete from server_log where entry_date </s", ('2018-03-01',))

cursor.close()
conn.commit()
conn.close()
