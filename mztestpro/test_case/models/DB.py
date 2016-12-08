import pymysql;
import sys


def delete_conn():
    conn=pymysql.connect(host='192.168.1.37',port=3307,user='smartstage',passwd='Uni-Ubi@SS2016',db='smartstage')
    cur=conn.cursor()
    print("连接成功")
    sql="""delete from uniubi_employee2 where name="1zheng_ceshi12" and state =2"""

    try:
        cur.execute(sql)
        conn.commit()
        print("删除成功")
    except Exception as e:
        conn.rollback()
        print(e)
        print("删除失败")

    conn.close()
#删除9个员工名字为zheng_ceshi1XX的元员工
def delete_conn2():
    conn=pymysql.connect(host='192.168.1.37',port=3307,user='smartstage',passwd='Uni-Ubi@SS2016',db='smartstage')
    cur=conn.cursor()
    print("连接成功")
    sql="""delete from uniubi_employee2 where name like "zheng_ceshi%" and state =2"""

    try:
        cur.execute(sql)
        conn.commit()
        print("删除成功")
    except Exception as e:
        conn.rollback()
        print(e)
        print("删除失败")

    conn.close()
if __name__=="__main__":
    delete_conn()


