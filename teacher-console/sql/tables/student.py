from commons import share
from sql.commons.db_operate import Connection

class Student():

    def selectAllStudents(self):
        con = Connection()
        sql = "select s.id, s.student_no, s.name, s.gender, s.age, c.name as belong_class, s.face_num" \
              " from student s" \
              " join class c on s.belong_class=c.id"
        data = con.cursor.execute(sql)
        # print("已经查出"+str(data)+"条数据!!!!")
        #
        # for item in con.cursor.fetchall():
        #     print(item)

        return con.cursor.fetchall()


    def loginMatch(self, student_no, password):
        con = Connection()
        sql = "select *" \
              " from student" \
              " where student_no=\'"+student_no+"\' and password=\'"+password+"\'"

        con.cursor.execute(sql)
        return con.cursor.fetchall()

    def addStudentFace(self):
        con = Connection()
        sql = "update student set face_num=20 where id=\'"+share.currentUser[0]+"\'"

        con.cursor.execute(sql)
        con.connect.commit()          #将事务提交

        return con.cursor.rowcount


    def deleteStudentFace(self):
        con = Connection()
        sql = "update student set face_num=0 where id=\'" + share.currentUser[0] + "\'"

        con.cursor.execute(sql)
        con.connect.commit()        # 将事务提交

        return con.cursor.rowcount


    def getStudent(self):
        con = Connection()
        sql = "select * from student where id=\'" + share.currentUser[0] + "\'"

        con.cursor.execute(sql)

        return con.cursor.fetchall()


    def modifyPassword(self, password):
        con = Connection()
        sql = "update student set password=\'" + password + "\' where id=\'" + share.currentUser[0] + "\'"

        con.cursor.execute(sql)
        con.connect.commit()  # 将事务提交

        return con.cursor.rowcount


    def selectAllStudentsByClass(self, class_name):
        con = Connection()
        sql = "select s.id, s.student_no, s.name, s.gender, s.age, c.name as belong_class, s.face_num" \
              " from student s" \
              " join class c on c.id=s.belong_class" \
              " where c.name=\'" + class_name + "\'"

        con = Connection()

        con.cursor.execute(sql)

        return con.cursor.fetchall()






if __name__ == '__main__':


    student = Student()
    print(student.selectAllStudentsByClass('移动三班'))