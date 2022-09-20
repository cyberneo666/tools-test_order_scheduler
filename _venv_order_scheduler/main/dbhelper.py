#数据库处理
import pymysql

conn=pymysql.connect(
    host="117.50.186.229",
    port=3306,
    user='root',
    password='Zpmc3261',
    database='test_order_assistant',
    charset='utf8'
)
cursor=conn.cursor()
def InsertNewIteration(startDate,endDate,iterationInfo):
    return ""
