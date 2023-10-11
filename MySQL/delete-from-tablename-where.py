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
            sql = "delete from runoob_tbl where runoob_id=9;"
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
