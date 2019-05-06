Import MySQLdb as db

conn = db.connect(host='localhost, user='root' , passwd ='PASSWORD'
cursor = conn.cursor()

cursor.execute("create database egdb)
cursor.execute('grant all privilies on egdb.* to 'egusuer'@'localhost' identified by 'PASSWORD')

cursor.close()
conn.commit()
conn.close()