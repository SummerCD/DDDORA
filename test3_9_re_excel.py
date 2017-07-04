# -*- coding:utf-8 -*-
import sys

from xlwt import Workbook

reload(sys)
sys.setdefaultencoding("UTF-8")
import urllib2
import re
import datetime
import xlwt
import xlrd


book = Workbook()
sheet1 = book.add_sheet('Hot',cell_overwrite_ok=True)
i = 1
sheet1.write(0,0,u'作者')
sheet1.write(0,1,u'内容')
sheet1.write(0,2,u'点赞')
page = 1
while page <= 10:
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    page +=1
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>(.*?)<div class="stats">.*?<i class="number">(.*?)</i>.*?</span>',re.S)
        items = re.findall(pattern,content)
        for item in items:
            haveImg = re.search("img",item[2])
            if not haveImg:
                j = 0
                sheet1.write(i,j,item[0])
                j += 1
                sheet1.write(i,j,item[1])
                j += 1
                sheet1.write(i,j,item[3])
                j += 1
                i += 1
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
file_name = "HotTop20-" + datetime.datetime.now().strftime('%Y%m%d%I%M%S')+".xls"
book.save(file_name)