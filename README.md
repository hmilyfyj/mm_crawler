#测试环境
 - py 2.7.9 Windows
 - py 2.7.1 Linux

#依赖
BeautifulSoup4

#usage
mm_crawler.py usage:                                                                                                                                                 
-h print help message.                                                                                                                                               
-n INTEGER:define num of thread.Default=10                                                                                                                           
-o PATH_STR:define dir for download.                                                                                                                                 
-l INTEGER:max images


#实现了
多线程、带参、可复用

#实现思想
1.初始化thread_max_num等关键变量。

2.检测是否带参，有则处理。否则使用默认配置。

3.crawl(url)：下载并保存该页面图片（过滤非相关图片）。并对页面超链的抓取，并将其存入任务队列page_que。

4.创建线程,线程从page_que获取url,并调用crawl（url)

5.步骤3.4循环往复直到相关变量达到定义的临界值，如:线程数量、下载图片数、用户发出中断。


#关于复用
修改crawl(url) get_url_prefix(url) get_host(url)三个函数中的正则匹配即可。

#缺点
没有使用代理IP。
没有设置header。
