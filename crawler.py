import sys
import io
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup


def getResponse(url):
    url=url
    req = request.Request(url)
    #req.add_header('cookie', cookie)
    #req.add_header('User-Agent',agent)
    resp = request.urlopen(req)
    html=resp.read().decode('utf-8')
    return html

if __name__ == '__main__':
    url='http://admin.m.arwawa.sklxsj.com/income/meitu_2018-06-07.log'
    #cookie = r'PHPSESSID=jnop2hrk1ef8ta5g58h9e3ksp0; login_type=oa'
    agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    html=getResponse(url)
    for line in html.split('\n'):
        print(line)
    print(html)