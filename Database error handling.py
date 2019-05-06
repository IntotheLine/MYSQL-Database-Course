import MySQLDB as db

try:
conn = db.connect(host='localhost', user='eguser', passwd ='PASSWORD', databse = 'egdb')
cursor = conn.cursor()
try:
cursor.execute("select * from server_log*)
record = cursor.fetchone()
while record is not None:
print(record)
record = cursor.fetchone()

exept db.Error as e:
print("Query error: " +str(e))
#cursor.rollback

cursor.close()
conn.close()
except db.Error as e:
print("Database error: " + str(ee))

