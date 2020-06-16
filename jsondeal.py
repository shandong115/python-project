import json
import os
from baidudeal import get_book2
import time
import traceback
import requests
import random

def get_fsids():
	#path = "E:\\documents\\book\\"
	path = "F:\\download\\baidunetdisk\\1\\"
	files = os.listdir(path)
	fsids=[]
	i = 0
	print(files)
	with open('out.txt', mode='w',encoding='utf-8') as f_out:
		for file in files:
			with open(path+file,mode='r',encoding='utf-8') as f:
				json_str = json.load(f)
				ll = json_str['list']
			
				for l in ll:
					fs_id = l['fs_id']
					fsids.append(fs_id)
					i=i+1
					if(i % 100 == 0):
						f_out.write(str(fsids))
						f_out.write('\n')
						fsids.clear()
						print('have dealed:'+str(i))
		if(len(fsids) > 0):
			f_out.write(str(fsids))
			f_out.write('\n')
			fsids.clear()
			print('have dealed:'+str(i))

def deal_json_file_and_get_book():
	#path = "E:\\documents\\book\\dlink\\4\\"
	path = "F:\\download\\baidunetdisk\\1\\"
	files = os.listdir(path)
	wrongs=[]
	#values=[]
	i = 0
	print(files)
	for file in files:
		with open(path+file,mode='r',encoding='utf-8') as f:
			json_str = json.load(f)
			ll = json_str['list']
		
			for l in ll:
				dlink = l['dlink']
				fileName=l['filename']
				
				data = get_book2(dlink)
				if(data is not None):
					with open('book\\'+fileName,'wb') as ff:
						ff.write(data)
					print(fileName+' is ok!\n')
				else:
					print('fail...'+str(l)+'\n')
					wrongs.append(l)
				time.sleep(2)
		print(file+' have dealed over!\n')
	with open('wrong.txt', mode='w',encoding='utf-8') as f_wrong:
		f_wrong.write(str(wrongs))
		
def get_dlink():
	url = 'https://pan.baidu.com/rest/2.0/xpan/multimedia?method=filemetas&access_token=121.91e183f3348a40588e9e85048079c998.YsJGWFef1mAN7VY10Au-496XoG3YJepFeAaTYFL.Xj0Ngg&dlink=1&fsids='
	
	ff = open('dlink.txt',mode='w',encoding='utf-8')
	with open('out.txt', mode='r', encoding='utf-8') as f:
		while(1):
			line = f.readline()
			if(len(line)<=0):
				break
			ff.write(url+line)
	ff.close()
	

def rename_files():
	#path = "E:\\documents\\book\\dlink\\4\\"
	#path = "E:\\workplace\\python-project\\book\\"
	path = "G:\\workspace\\python\\python-project\\book\\"
	files = os.listdir(path)
	print('file numbers:'+str(len(files))+'\n')
	s1 = 'obook.cc-'
	s2 = 'SoBooKs.cc - '
	s3 = 'obook.cc - '
	s4 = 'obook.cc'
	newName=''
	with open('1.txt','a',encoding='utf-8') as f:
		for file in files:
			newName=''
			if(file.startswith(s1)):
				newName = file[len(s1):]
			elif(file.startswith(s2)):
				newName = file[len(s2):]
			elif(file.startswith(s3)):
				newName = file[len(s3):]
			elif(file.startswith(s4)):
				newName = file[len(s4):]
				
			if(len(newName)>0):
				try:
					os.rename(path+file, path+newName)
					f.write('oldname:'+file+'--->newName:'+newName+'\n')
				except FileExistsError as e:
					print('FileExistsError Exception!'+file)
					traceback.print_exc()
		
def send_file_name():
	path = "G:\\workspace\\python\\python-project\\book\\"
	#path = "E:\\workplace\\python\\python-project\\book\\"
	#path = "D:\\download\\chrome\\"
	files = os.listdir(path)
	random.shuffle(files)
	for file in files:
		if(os.path.isfile(path+file) and file.endswith('.epub')):
			index=file.find('.epub')
			r=requests.get('http://127.0.0.1:8888',params={'fullname':path+file,'filename':file[:index]})
			print('send file:'+file+' ,status:'+str(r.status_code))
			time.sleep(1)
	
if __name__ == '__main__':
	deal_json_file_and_get_book()
	#get_fsids()
	#rename_files()
	#send_file_name()