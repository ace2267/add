import pymysql

conn = pymysql.connect(host='192.168.1.252', port=33060 ,user='root', password='test',db='test', charset='utf8')
 
try:
# INSERT
   with conn.cursor() as curs:
      sql = "insert into board(userName,contents) values (%s, %s)"
      curs.execute(sql, ('이광수', '서울'))

      conn.commit()
 
# SELECT
   with conn.cursor() as curs:
      sql = "select * FROM board"
      curs.execute(sql)
      rs = curs.fetchall()
      for row in rs:
         print(row)
 
finally:
      conn.close()