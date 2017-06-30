# -*- coding:utf-8 -*-
import urllib
import urllib2
import re



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
                print "作者：",item[0]
                print "内容：",item[1]
                print "评论数：",item[3]
                print "\n----------------------------------------------------------------------------------------------------------------------------------\n"
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason