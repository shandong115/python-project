import os
import datetime
import requests
import brotli
#import codes
#from codes import dict_codes
import traceback
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from lxml import etree
import time

def get_baidu_data(url):
	
	headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'
			}
	try:
		response = requests.get(url, headers=headers,timeout=30)
		if not response.status_code == 200:
			print('Request Not Successfully: '+url + ',======>status_code:'+str(response.status_code))
			return None
		print('Request Successfully: ' + url)
	except RequestException as e:
		print('Request Exception!'+url)
		traceback.print_exc()
		return None
		
	key = 'Content-Encoding'
	if(key in response.headers and response.headers['Content-Encoding'] == 'br'):
		data = brotli.decompress(response.content)
		data1 = data.decode('utf-8')
		return(data1)
	else:
		return(response.text)
	
def get_book(url):
	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'en-US,en;q=0.5',
		'Connection':'keep-alive',
		'DNT':'1',
		'Host':'pan.baidu.com',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
		}
	try:
		response = requests.get(url, headers=headers,timeout=30)
		if not response.status_code == 200:
			print('Request Not Successfully: '+url + ',======>status_code:'+str(response.status_code))
			return None
		print('Request Successfully: ' + url)
	except RequestException as e:
		print('Request Exception!'+url)
		traceback.print_exc()
		return None
		
	key = 'Content-Encoding'
	if(key in response.headers and response.headers['Content-Encoding'] == 'br'):
		data = brotli.decompress(response.content)
		data1 = data.decode('utf-8')
		return(data1)
	else:
		return(response.text)
		
if __name__ == '__main__':
	#url='https://pan.baidu.com/rest/2.0/xpan/multimedia?method=filemetas&access_token=121.91e183f3348a40588e9e85048079c998.YsJGWFef1mAN7VY10Au-496XoG3YJepFeAaTYFL.Xj0Ngg&&fsids=[881468097891744,404815862929782]&dlink=1'
	url='https://d.pcs.baidu.com/file/6869b32c7oc5f700291f1aba2e48a59f?fid=587978346-250528-16517637562495\u0026rt=pr\u0026sign=FDtAERV-DCb740ccc5511e5e8fedcff06b081203-mQTWPv%2Fx0PxFu1OSXKQULNwYG0c%3D\u0026expires=8h\u0026chkbd=0\u0026chkv=2\u0026dp-logid=825729390285808726\u0026dp-callid=0\u0026dstime=1591293640\u0026r=569257331'
	data=get_book(url)
	print(data)