#coding:utf-8
import urllib2
import re
import sys,getopt
import os
from bs4 import BeautifulSoup
import threading
from Queue import Queue
from time import sleep

page_que = Queue()
thread_max_num = 10 #最大进程数
host='http://www.22mm.cc/mm/qingliang/' #爬取地址
dir='pics' #下载目录
img_count=0 #已下载图片数目
img_max_num=0 #最大下载图片数目
mutex=threading.Lock() #数目锁



#保存图片
def save_img_by_url(url,path="./pics/"):
	if not os.path.exists(path):
		os.makedirs(path)
		
	img=urllib2.urlopen(url).read()
	filename=url.split("/")[-1]
	if os.path.exists(path+"/"+filename):
		print 'pic existed\n'
		return 0
	f=open(path+"/"+filename,'wb+')
	f.write(img)
	f.close
	return 1
	

#获取html
def get_soup_html(url):
	html=urllib2.urlopen(url).read();
	soup=BeautifulSoup(html)
	return soup
	
#获取图片并下载。
def get_img(soup):
	global img_count,img_max_num,mutex
	for img in soup.findAll('img',src=True):
		if re.findall(r'\d+_\d+',img['src']):
			imgurl=img['src']
			print imgurl
			print "第%d次\n"%img_count
			result=save_img_by_url(imgurl,dir)
			if result==1:
				mutex.acquire()
				img_count=img_count+1
				mutex.release()
			if(img_count>img_max_num and not img_max_num==0):
				print "reach the img_max_num，thread exited\n"
				sys.exit(0)

#获取网址的最后一个/之前的部分			
def get_url_prefix(url):
	partten=r'([^"]*/)\w*(\.)\w*$'
	m=re.match(partten,url)
	if m:
		return get_host(url)
	else:
		return url
		
#获取域名			
def get_host(url):
	partten=r'([^".]*\w\w*\.\w*.\w*)/*[^"]*'
	host=re.match(partten,url).groups()[0]
	return host+"/"
	
#抓取
def crawl(url):
	soup=get_soup_html(url)
	get_img(soup)
	host=get_host(url)
	url=get_url_prefix(url)
	#获取详细页面超链接。
	for a in soup.findAll('a',href=True):
		if re.findall(r'^/[^"]*/[^"t]+/[^"t]*\.html',a['href']):
			newurl=host+a['href']
			page_que.put(newurl)
					
	#获取下一页超链接
	div=soup.find(class_='ShowPage')
	if div:
		newurl=url+div.a['href']
		#crawl(newurl)
		page_que.put(newurl)

		
#子线程调用该函数。		
def work():
	url=page_que.get()
	crawl(url)


#命令行帮助
def usage():
		print 'mm_crawler.py usage:'
		print '-h print help message.'
		print '-n INTEGER:define num of thread.Default=10'
		print '-o PATH_STR:define dir for download.'
		print '-l INTEGER:max images'

#处理命令行参数
def para_handler(argv):
	try:
		opts,args=args = getopt.getopt(argv[1:],'hn:o:l:')
	except getopt.GetoptError, err:
		print str(err)
		usage()
		
	for o,a in opts:
		if o in('-h'):
			usage()
			sys.exit(1)
		elif o in('-n'):
			global thread_max_num
			print a
			thread_max_num=int(a)
			print thread_max_num
		elif o in('-o'):
			global dir
			dir=a
			print dir
		elif o in('-l'):
			global img_max_num
			img_max_num=int(a)
			print img_max_num
#测试	    
def main(argv):
	para_handler(argv)
	crawl(host)
	while page_que.qsize()>0 and img_count<=img_max_num or img_max_num==0:
		while threading.activeCount()<=thread_max_num:
			t=threading.Thread(target=work)
			t.setDeamon(True)
			t.start()
	
if __name__=='__main__':
	main(sys.argv)
