#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
from lxml import html
import urllib
import urllib2
import datetime

page = 1
url = 'https://www.qiushibaike.com/hot/'+str(page)
user_agent =  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
headers = {'User-Agent':user_agent} #{}

request = urllib2.Request(url,headers=headers)
respose = urllib2.urlopen(request)
str_html = respose.read()
respose.close()

tree = html.fromstring(str_html)
nodes = tree.xpath('//div[@id="content-left"]/div[@class="article block untagged mb15"]')

file_name = "./HotTop20-" + datetime.datetime.now().strftime('%Y%m%d%I%M%S') + ".txt"
info_file =open(file_name,"w")
info_file.write("作者,年龄,内容,点赞,评论\n")
for node in nodes:
    res_author = node.xpath('div[@class="author clearfix"]/a[2]/h2')[0].text
    res_age = node.xpath('div[@class="author clearfix"]/div[@class]|div[@class="author clearfix"]/span[2]/h2')[0].text
    content = node.xpath('a[@class="contentHerf"]/div[@class="content"]/span')[0].text
    num_vote = node.xpath('div[@class="stats"]/span[@class="stats-vote"]/i')[0].text
    num_comments = node.xpath('div[@class="stats"]/span[@class="stats-comments"]/a[@class="qiushi_comments"]/i')[0].text
    info_file.write(res_author)
    info_file.write(',')
    info_file.write(res_age)
    info_file.write(',')
    info_file.write(content)
    info_file.write(',')
    info_file.write(num_vote)
    info_file.write(',')
    info_file.write(num_comments)
    info_file.write("\n")
file_name.close()

#糗事百科xpath提取