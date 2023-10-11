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
            value = "(8,'学习SQL','SQL_USER',now()),(9,'学习Django','Django_USER',now())"
            sql = f"insert into runoob_tbl values {value};"
            cursor.execute(sql)

            con.commit()
            print("提交成功！")

    except Exception as e:
        con.rollback()
        print("数据库异常\n",e)
    finally:
        con.close()


if __name__ == '__main__':
    mysql_db()
    print('连接成功数据库！')
