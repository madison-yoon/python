import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="1234", database="mysqlDB", charset="utf8")
cur = conn.cursor()

def select_sql():
    cur.execute("SELECT * FROM userTable")
    rows = cur.fetchall()

    print("   ID        PASSWORD        이름           이메일             주소")
    print("-----------------------------------------------------------------------")
    for row in rows:
        id, pwd, name, mail, addr = row
        print(f"{id:10} {pwd:12} {name:10} {mail:15} {addr:30}")

    conn.close()

select_sql()