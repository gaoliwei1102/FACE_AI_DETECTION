import pymysql.cursors
# 获取mysql连接，连接到数据库

class Connection():

    def __init__(self):

        self.connect = pymysql.Connect(
            host='localhost',   # mysql的服务器地址
            port=3306,          # mysql服务器地址的端口号
            user='root',        # 用户名
            passwd='root',      # 密码
            db='test_ai',       # 数据库名称
            charset='utf8'      # 字符集编码
        )

        # 获取到数据库游标
        self.cursor = self.connect.cursor()


