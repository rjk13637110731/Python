import pymysql
from MysqlConfig import MysqlConfig


class MysqlConnection:
    def __init__(self, host=MysqlConfig.host, port=MysqlConfig.port, user=MysqlConfig.user, pwd=MysqlConfig.password,
                 db=MysqlConfig.db):
        self.db = pymysql.connect(host=host, port=port, user=user, password=pwd, database=db,
                                  charset=MysqlConfig.charset)
        self.cursor = self.db.cursor()

    def query(self, sql, many=True):
        try:
            self.cursor.execute(sql)
            if many:
                res = self.cursor.fetchall()
            else:
                res = self.cursor.fetchone()
            return res
        except Exception as e:
            raise e

    def __do(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            self.db.rollback()
            raise e
        else:
            self.db.commit()

    def update(self, sql):
        self.__do(sql)

    def insert(self, sql):
        self.__do(sql)

    def delete(self, sql):
        self.__do(sql)

    def exit(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    db = MysqlConnection()
    res = db.query('select * from runoob_tbl;')
    print(res)
    db.exit()
