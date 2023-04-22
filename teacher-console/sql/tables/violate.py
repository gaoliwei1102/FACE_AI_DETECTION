from commons import share
from sql.commons.db_operate import Connection

class Violate():

    def selectAllViolate(self):
        con = Connection()
        sql = "select * from violate"


        data = con.cursor.execute(sql)
        # print("已经查出"+str(data)+"条数据!!!!")
        #
        # for item in con.cursor.fetchall():
        #     print(item)

        return con.cursor.fetchall()


    def insertViolate(self, violate):
        con = Connection()
        sql = "insert into violate (id, type, course, student, remarks, create_time) values ('%s', '%s', '%s', '%s', '%s', '%s')"

        result = con.cursor.execute(sql%violate)

        con.connect.commit()

        return result



if __name__ == '__main__':
    violate = Violate()
    user = ('a8982c82bac211ec972400f48d58f7a4', '567ecade86f14e4da698fcf6a79f8013', '8d4126c5b9a644d89cfeb30c021f7f1f', '263d47552442480181671e4c3bf17ba1', '中途离开课堂', '2022-04-13 08:42:55')
    violate.insertViolate(user)