# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
import urllib2
import re
import datetime
import os


file_name = "./HotTop20-" + datetime.datetime.now().strftime('%Y%m%d%I%M%S') + ".txt"
info_file =open(file_name,"w")
info_file.write("作者,内容,评论数\n")
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
                info_file.write(item[0])
                info_file.write('\t')
                info_file.write(item[1])
                info_file.write('\t')
                info_file.write(item[3])
                info_file.write("\n")
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
info_file.close()