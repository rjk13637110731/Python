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


if __name__ == '__main__':
    mysql_db()
    print('连接成功数据库！')
