#-*- coding: utf-8 -*-
import requests
import re
import time
import os
def spi(my_proxy,keywd,headers):
	print "[start] apkpure keywd="+keywd
	success_list=[]
	with open('./apkpure/'+keywd+'.txt','w+') as file:
		success_list=file.read()
	file.close()
	success_list=success_list.split('\n')
	pattern =re.compile(r'<span>(\d+)</span>\ search\ results',re.S)
	dw_pattern = re.compile(r'<a\ id="download_link".*?href="(.*?)">',re.S)	
	list_pattern = re.compile(r'<dt><a\ title="(.*?)".*?href="(.*?)">',re.S)
	url = "https://apkpure.com/search?q="+keywd
	r= requests.get(url,proxies=my_proxy,timeout=5,headers=headers)
	base_search_url = "https://apkpure.com/search-page?q="+keywd+"&begin=" 
	dw_base_url = "https://apkpure.com"
	nr_app = re.search(pattern,r.content)
	if(nr_app is not None):
		nr_app = nr_app.group(1)
	nr_time = int(nr_app)/15
	if(int(nr_app)%15>0):
		nr_time +=1
	
	print str(nr_app)+" totally found, getting download url"
	download_url={}


#############################################################
#modify to change the num of pages of apps u want to download 
	nr_time=1

#############################################################



	for i in range(0,nr_time):
		try:
			content=requests.get(base_search_url+str(i*15),proxies=my_proxy,timeout=5,headers=headers).content
		except:
			print "error in getting download_url "+base_search_url+str(i*15)
		if content is not None:
			result = re.findall(list_pattern,content)
		else:
			 result=[]
		for item in result:
			download_url[item[0]]=dw_base_url+item[1]+'/download'
	
	with open('./apkpure/app.txt','w') as file:
		for item in download_url:
			file.write(item+' '+download_url[item]+'\n')
	file.close()
	print "getting real download_url"
	count =0	
	for i in download_url:
		print download_url[i]
		if download_url[i] in success_list:
			continue
		try:
			content=requests.get(download_url[i],proxies=my_proxy,timeout=5,headers=headers).content
		except:
			print "error in open url"
			download_url[i]=None
			continue
		if content is not None:
			result=re.search(dw_pattern,content)
		else:
			 result=None
		if(result is not None):
			count+=1
			print count
			download_url[i]=result.group(1)
			time.sleep(0.1)
		else:
			print "error in match content"
			download_url[i]=None
			continue
	#print download_url	
	if os.path.isdir('./apkpure/apk') is False:
		os.makedirs('./apkpure/apk')

	for item in download_url:
	#######################################################################
	#here to modify the timeout ofdownloading app , default value is 300
	#######################################################################
		if download_url[item]==None:
			continue
		try:
			apk=requests.get(download_url[item],proxies=my_proxy,timeout=300)
		except:
			print "error in download app "+item
			continue
		if os.path.isdir('./apkpure/apk/'+keywd) is False:
			os.makedirs('./apkpure/apk/'+keywd)
		with open('./apkpure/apk/'+keywd+'/'+item+'.apk',"wb") as file:
			for chunk in apk.iter_content(chunk_size=1024):
				if chunk:
					file.write(chunk)
		print "finish download "+item
		with open('./apkpure/'+keywd+'.txt','a+') as file:
			file.write(item+'\n')
		file.close()


