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
import urllib.request
from urllib.error import HTTPError
import http

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
	#headers = {
	#	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	#	'Accept-Encoding':'gzip, deflate, br',
	#	'Accept-Language':'zh-CN,zh;q=0.9',
	#	'Cache-Control':'max-age=0',
	#	'Connection':'keep-alive',
	#	'Cookie':'BIDUPSID=a1058bf4dc003808d203c98e1507ba4c; PSTM=1590161023; BAIDUID=a1058bf4dc003808d203c98e1507ba4c:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=GloU09uQ1dnOWt3ak1ZZlc4MHZXeU9Cb0dGU2E0Zm1vLWtKdzA1dWdRU2I1QUJmSVFBQUFBJCQAAAAAAAAAAAEAAACYI7UPycC2rDExNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJtX2V6bV9led; PANWEB=1; STOKEN=151a77864dbc018403d047d3c1cca2dc008164375d2fcf528ee61592d225050a; SCRC=044b165dc988c55c1c0e3dcae4eeeddd; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; jshunter-uuid=4a998b5a-55c7-459e-abc2-532d9b46aaa6; csrfToken=ZV3tb9G1NSWpxjPiq7tb_qLI; H_PS_PSSID=31727_1431_31326_21079_31606_31779_31673_31322_30824_31846',
	#	'Host':'pan.baidu.com',
	#	'Sec-Fetch-Dest':'document',
	#	'Sec-Fetch-Mode':'navigate',
	#	'Sec-Fetch-Site':'none',
	#	'Sec-Fetch-User':'?1',
	#	'Upgrade-Insecure-Requests':'1',
	#	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	#}
	
	
	headers = {'Cookie': 'BIDUPSID=a1058bf4dc003808d203c98e1507ba4c; PSTM=1590161023; BAIDUID=a1058bf4dc003808d203c98e1507ba4c:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=GloU09uQ1dnOWt3ak1ZZlc4MHZXeU9Cb0dGU2E0Zm1vLWtKdzA1dWdRU2I1QUJmSVFBQUFBJCQAAAAAAAAAAAEAAACYI7UPycC2rDExNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJtX2V6bV9led; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; jshunter-uuid=4a998b5a-55c7-459e-abc2-532d9b46aaa6'}
	
	try:
		response = requests.get(url, headers=headers)
		#response = requests('GET',  url, headers=headers)
		#print(response.text)
		#reditList = response.history
		#print(response.history)
		if not response.status_code == 200:
			print('Request Not Successfully: ['+url + '],======>status_code:'+str(response.status_code))
			print(headers)
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
		#return(response.text)
		return(response.content)
		
def get_book2(url):
	headers = {'Cookie': 'BIDUPSID=a1058bf4dc003808d203c98e1507ba4c; PSTM=1590161023; BAIDUID=a1058bf4dc003808d203c98e1507ba4c:FG=1; PANWEB=1; BDUSS=FoWjZMZmZkUHc2R1VxNkhsZktnaEl1Tm1HRDdhbXU5SlJZOXpJeHptWENaQXhmRVFBQUFBJCQAAAAAAAAAAAEAAACYI7UPycC2rDExNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMLX5F7C1-ReTX; STOKEN=4c2c6c865c7e376e7f2e8ceaba68392e56c745e261d23d0cc611c189c6802d77; SCRC=6791d066dc8b10c20b8d25469a015294; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1592055750; yjs_js_security_passport=4610ed0149cf26d8d417ebe6f22b6eebe0bc7228_1592499082_js; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'} 
	#headers = {'Cookie': 'BIDUPSID=a1058bf4dc003808d203c98e1507ba4c; PSTM=1590161023; BAIDUID=a1058bf4dc003808d203c98e1507ba4c:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=GloU09uQ1dnOWt3ak1ZZlc4MHZXeU9Cb0dGU2E0Zm1vLWtKdzA1dWdRU2I1QUJmSVFBQUFBJCQAAAAAAAAAAAEAAACYI7UPycC2rDExNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJtX2V6bV9led; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; jshunter-uuid=4a998b5a-55c7-459e-abc2-532d9b46aaa6;'} 
	try:
		request=urllib.request.Request(url,headers=headers)
		rsp = urllib.request.urlopen(request)
		if(rsp.status == 200):
			print("get success. reading....")
			return rsp.read()
		else:
			print("fail...code="+str(rsp.status))
			return None
	except HTTPError as e:
		print('Request Exception!'+url)
		traceback.print_exc()
		return None
	except ConnectionResetError as e:
		print('Request ConnectionResetError!'+url)
		traceback.print_exc()
		return None
	except TimeoutError as e:
		print('Request TimeoutError!'+url)
		traceback.print_exc()
		return None	
	except OSError as e:
		print('Request OSError!'+url)
		traceback.print_exc()
		return None	
	except urllib.error.URLError as e:
		print('Request URLError!'+url)
		traceback.print_exc()
		return None	
	except http.client.IncompleteRead as e:
		print('Request http.client.IncompleteRead!'+url)
		traceback.print_exc()
		return None	
	
	
	
		
#if __name__ == '__main__':
	#url="https://d.pcs.baidu.com/file/4b564b91bv8ca50122946c324f5779c9?fid=587978346-250528-19210837918619&rt=pr&sign=FDtAERV-DCb740ccc5511e5e8fedcff06b081203-VrDi%2FB%2Fd6EjC1hwUjqQi%2B45rtDA%3D&expires=8h&chkbd=0&chkv=2&dp-logid=4108434491219458472&dp-callid=0&dstime=1591369415&r=805497289"
	#url="https://pan.baidu.com/rest/2.0/xpan/multimedia?method=filemetas&access_token=121.91e183f3348a40588e9e85048079c998.YsJGWFef1mAN7VY10Au-496XoG3YJepFeAaTYFL.Xj0Ngg&dlink=1&fsids=%5B451941592623457,207948535100295%5D"
	
	#url="https%3A%2F%2Fpan.baidu.com%2Frest%2F2.0%2Fxpan%2Fmultimedia%3Fmethod%3Dfilemetas%26access_token%3D121.91e183f3348a40588e9e85048079c998.YsJGWFef1mAN7VY10Au-496XoG3YJepFeAaTYFL.Xj0Ngg%26dlink%3D1%26fsids%3D%5B451941592623457%2C207948535100295%5D"
	#data=get_book(url)
	#if(data is not None):
	#	with open('e.txt','w') as f:
	#		f.write(data)
	#else:		
	#	print('wrong...')
		
	
