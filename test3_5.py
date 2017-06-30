#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib2
from lxml import html
import datetime

page = 1
count = 0
name = []
age = []

url = 'https://www.qiushibaike.com/hot/'+ str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
headers={'User-Agent':user_agent}

request = urllib2.Request(url,headers=headers)
respose = urllib2.urlopen(request)
str_html = respose.read()
respose.close()

tree = html.fromstring(str_html)
nodes = tree.xpath('//div[@id="content-left"]/div[@class="article block untagged mb15"]')

filename="./HotTop20-"+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.txt'
info_file = open(filename,'w')

for node in nodes:
    res_author = node.xpath('div[@class="author clearfix"]/a[2]/h2')[0].text
    res_age = node.xpath('div[@class="author clearfix"]/div[@class]')[0].text
    info_file.write(res_author)
    info_file.write(',')
    info_file.write(res_age)
    info_file.write("\n")


info_file.close()
