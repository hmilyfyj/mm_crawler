#���Ի���
 - py 2.7.9 Windows
 - py 2.7.1 Linux

#����
BeautifulSoup4

#usage
mm_crawler.py usage:                                                                                                                                                 
-h print help message.                                                                                                                                               
-n INTEGER:define num of thread.Default=10                                                                                                                           
-o PATH_STR:define dir for download.                                                                                                                                 
-l INTEGER:max images


#ʵ����
���̡߳����Ρ��ɸ���

#ʵ��˼��
1.��ʼ��thread_max_num�ȹؼ�������

2.����Ƿ���Σ�����������ʹ��Ĭ�����á�

3.crawl(url)�����ز������ҳ��ͼƬ�����˷����ͼƬ��������ҳ�泬����ץȡ������������������page_que��

4.�����߳�,�̴߳�page_que��ȡurl,������crawl��url)

5.����3.4ѭ������ֱ����ر����ﵽ������ٽ�ֵ����:�߳�����������ͼƬ�����û������жϡ�


#���ڸ���
�޸�crawl(url) get_url_prefix(url) get_host(url)���������е�����ƥ�伴�ɡ�

#ȱ��
û��ʹ�ô���IP��
û������header��
