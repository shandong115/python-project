import json
import os

def get_fsids():
	path = "E:\\documents\\book\\"
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
	
if __name__ == '__main__':
	get_dlink()