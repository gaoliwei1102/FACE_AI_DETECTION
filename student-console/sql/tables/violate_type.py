from commons import share
from sql.commons.db_operate import Connection

class ViolateType():

    def selectAllViolateType(self):
        con = Connection()
        sql = "select * from violate_type"


        data = con.cursor.execute(sql)
        # print("已经查出"+str(data)+"条数据!!!!")
        #
        # for item in con.cursor.fetchall():
        #     print(item)

        return con.cursor.fetchall()


if __name__ == '__main__':
    violateType = ViolateType()
    print(violateType.selectAllViolateType())