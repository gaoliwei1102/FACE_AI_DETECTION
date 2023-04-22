from commons import share
from sql.commons.db_operate import Connection

class Violate():

    def selectMyAllViolates(self):
        con = Connection()

        sql = "select v.id, vt.name as type, v.course, v.student, v.remarks, v.create_time from violate v" \
              " join violate_type vt on vt.id=v.type" \
              " where student=\'" + share.currentUser[0] + "\'"

        con.cursor.execute(sql)

        return con.cursor.fetchall()


if __name__ == '__main__':
    # student = Student()
    # print(student.loginMatch("181164276", "123456"))

    violate = Violate()
    # print(violate.selectMyAllViolates("263d47552442480181671e4c3bf17ba1"))