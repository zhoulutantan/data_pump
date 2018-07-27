from urllib import request
import time



def get_url_response(url):
    url=url
    req = request.Request(url)
    #req.add_header('cookie', cookie)
    #req.add_header('User-Agent',agent)
    resp = request.urlopen(req)
    html=resp.read().decode('utf-8')
    return html

def date_trans(date,date_format):
    date_str=''
    date_str=time.strptime(date,"%Y-%m-%d")
    strTime = time.strftime(date_format, date_str)
    return strTime



if __name__ == '__main__':
    # url='http://admin.m.arwawa.sklxsj.com/income/meitu_2018-06-07.log'
    # #cookie = r'PHPSESSID=jnop2hrk1ef8ta5g58h9e3ksp0; login_type=oa'
    # agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    # html=get_url_response(url)
    # for line in html.split('\n'):
    #     print(line)
    #
    # d=date_trans('2018-06-10',"%Y%m%d")
    # print(d)

    import pandas as pd
    from sqlalchemy import create_engine

# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：mydb



