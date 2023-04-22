from commons import share
from sql.commons.db_operate import Connection

class Course():

    def selectMyAllCourses(self):
        con = Connection()
        sql = "select c.id, s.name as subject, t.name as teacher, tc.name as tbl_class, c.start_day, c.start_time, c.end_time, c.remarks from course c" \
              " join subject s on c.subject=s.id" \
              " join teacher t on c.teacher=t.id" \
              " join class tc on c.tbl_class=tc.id" \
              " where c.teacher=\'" + share.currentUser[0] + "\'" \
              " order by c.start_day,c.start_time" \


        data = con.cursor.execute(sql)
        # print("已经查出"+str(data)+"条数据!!!!")
        #
        # for item in con.cursor.fetchall():
        #     print(item)

        return con.cursor.fetchall()


    def selectMyAllCoursesByName(self, name):
        con = Connection()
        sql = "select c.id, s.name as subject, t.name as teacher, tc.name as tbl_class, c.start_day, c.start_time, c.end_time, c.remarks from course c" \
              " join subject s on c.subject=s.id" \
              " join teacher t on c.teacher=t.id" \
              " join class tc on c.tbl_class=tc.id" \
              " where c.teacher=\'" + share.currentUser[0] + "\' and s.name like \'%" + name + "%\'" \
              " order by c.start_day,c.start_time" \


        data = con.cursor.execute(sql)
        # print("已经查出"+str(data)+"条数据!!!!")
        #
        # for item in con.cursor.fetchall():
        #     print(item)

        return con.cursor.fetchall()