#-*- coding: UTF-8 -*-

import  urllib
import urllib2
from lxml import html
import os

page = 1
count = 0
name = []
age = []
url = 'http://www.qiushibaike.com/hot/page/'+ str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
headers={'User-Agent':user_agent}

request = urllib2.Request(url,headers=headers)
respose = urllib2.urlopen(request)
str_html = respose.read()
respose.close()

tree = html.fromstring(str_html)
nodes = tree.xpath('//div[@id="content-left"]/div[@class="article block untagged mb15"]')
info_file = open('./info.txt','w')
for node in nodes:
    res_author = node.xpath('div[@class="author clearfix"]/a[2]/h2')[0]
    res_age = node.xpath('div[@class="author clearfix"]/div[@class]')[0]
    info_file.write(res_author.text)
    info_file.write(res_age.text)
    info_file.write("\n")
    print res_author.text,
    print ",",
    print res_age.text
info_file.close()