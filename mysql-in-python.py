import MySQLdb
import csv

cnx = MySQLdb.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='cadastro')
cursor = cnx.cursor()
cursor.execute("SELECT nome, descricao, carga, totaulas, ano FROM cursos")
data = cursor.fetchall()

for row in data:
    print(row[0], row[1], row[2], row[3], row[4])

    with open('log-mysql.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        for row in data:
            spamwriter.writerow(row)

cnx.close()
