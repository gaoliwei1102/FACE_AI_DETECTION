from commons import share
from sql.commons.db_operate import Connection

class Class():

    def selectAllClasses(self):
        con = Connection()
        sql = "select * from class"


        data = con.cursor.execute(sql)
        # print("已经查出"+str(data)+"条数据!!!!")
        #
        # for item in con.cursor.fetchall():
        #     print(item)

        return con.cursor.fetchall()


    def selectAllClassById(self, id):
        con = Connection()
        sql = "select * from class where id=\'" + id + "\'";


        data = con.cursor.execute(sql)
        # print("已经查出"+str(data)+"条数据!!!!")
        #
        # for item in con.cursor.fetchall():
        #     print(item)

        return con.cursor.fetchall()