#应用实例
#(base) G:\workspace\python\python-project\iqiyi>python dealfilename.py "G:\qycache\download\亲子课堂章卫\mp4 - 3" _ .mp4
import os
import sys

dir=sys.argv[1]
s1=sys.argv[2]
s2=sys.argv[3]
filename=''
fileNum=0
changeNum=0
print("dir is %s"%dir)
print("s1 is %s"%s1)
print("s2 is %s"%s2)
os.chdir(dir)
for ss in os.listdir("."):
	print(ss)
	try:
		n1=ss.index(s1)
		n2=ss.index(s2)
		fileNum=fileNum+1
		if(n1>=0 and n2>0):
			filename=ss[0:n1]
			filename+=ss[n2:]
			print(filename)
			os.rename(ss, filename)
			changeNum=changeNum+1
	except ValueError:
		print("ValueError")
	except WindowsError:
		print("windows error")
	else:
		print("rename ok!")
print("fileNum:"+str(fileNum))
print("changeNum:"+str(changeNum))
