from commons import share
from sql.commons.db_operate import Connection


class Teacher():

    def matchLogin(self, teacherNo, password):
        con = Connection()

        sql = "select id, teacher_no, password, name, age, gender, phone, email from teacher" \
              " where teacher_no='%s' and password='%s'"

        con.cursor.execute(sql%(teacherNo, password))

        return con.cursor.fetchall()

    def modifyPassword(self, password):
        con = Connection()
        sql = "update teacher set password=\'" + password + "\' where id=\'" + share.currentUser[0] + "\'"

        con.cursor.execute(sql)
        con.connect.commit()  # 将事务提交

        return con.cursor.rowcount

    def getTeacher(self):
        con = Connection()
        sql = "select * from teacher where id=\'" + share.currentUser[0] + "\'"

        con.cursor.execute(sql)

        return con.cursor.fetchall()

if __name__ == '__main__':

    teacher = Teacher()
    print(teacher.matchLogin("11020001", "13456"))