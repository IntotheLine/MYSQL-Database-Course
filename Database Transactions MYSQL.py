import MySQLDB as db

conn = db.connect(host='localhost', user='eguser', passwd ='PASSWORD', databse = 'egdb')
cursor = conn.cursor()

try:
for i in range(1,2):
	print(f'updating row: {i}')
	cursor.execute("update server_log set entry_date = now() where log_id = %s, (i,))
	print(f'rows updated: {cursor.rowcount}')
	if cursor.rowcount == 0:
	raise ValueError(f'row not updated: {i}')
	print()
	cursor.close()
	conn.commit()

except Exception as e:
print('rolling back')
print(str(e))
conn.rollback()

cursor.close()
conn.close()


