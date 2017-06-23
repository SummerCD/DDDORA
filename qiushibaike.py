#-*- coding: UTF-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent =  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url,headers=headers)
    respose = urllib2.urlopen(request)
    content = respose.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2></a><div class="articleGender .*?>(.*?)</div>.*?<a.*?class="contentHerf"><div class="content"><span>(.*?)</span></div></a>(.*?)<div class="stats"><span.*?<i class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

