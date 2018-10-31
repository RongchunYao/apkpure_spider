#-*- coding: utf-8 -*-
import requests
import my_conf
import apkpure.apkpure as apkpure
if __name__=="__main__":
	re= apkpure.spi(my_conf.my_proxy,my_conf.key_wd[0],my_conf.my_headers)
	print(re)
