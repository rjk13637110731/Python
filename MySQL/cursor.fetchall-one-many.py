import pymysql


def mysql_db():
    con = pymysql.connect(
        host='localhost',
        port=3306,
        database='runoob',
        charset='utf8',
        user='root',
        password='123456'
    )

    try:
        with con.cursor() as cursor:
            sql = "select * from runoob_tbl;"
            cursor.execute(sql)

            datas = cursor.fetchall()
            print("获取的数据：\n",datas)
            
            datas = cursor.fetchone()
            print("获取的数据：\n",datas)
            
            datas = cursor.fetchmany(3)
            print("获取的数据：\n",datas)
    except Exception as e:
        print("数据库异常\n",e)
    finally:
        con.close()


if __name__ == '__main__':
    mysql_db()
    print('连接成功数据库！')
