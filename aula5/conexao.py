import MySQLdb

try:
	con = MySQLdb.connect(host='localhost', db='gotham', user='robin', passwd='Gotham@123')
	print('Conectou')
	cur = con.cursor()
except Exception as e:
	print('Erro: {}'.format(e))