import pymysql as mysql

con = mysql.Connect(host='localhost', user='root', passwd='', db='pitu_pitu')

# cur = con.cursor()


# cur.execute("use dziennikluty23")
# zapytanieWyswietl = cur.execute("show tables")
# cur.close()


wbd = con.cursor()

wbd.execute("SELECT * FROM `users`")

for record in wbd:
    print(record)

wbd.close()
# con.commit()
# cur.close()