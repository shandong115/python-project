# -*- encoding:utf-8 -*-
import os
import sys
#s1='——'
s1='三优亲子'
s2='.mp4'
filename=''
fileNum=0
changeNum=0
dir=sys.argv[1]
print("dir is %s"%dir)
os.chdir(dir)
for ss in os.listdir("."):
	print ss
	try:
		n1=ss.index(s1)
		print("n1=%d"%n1)
		n2=ss.index(s2)
		print("n2=%d"%n2)
		fileNum=fileNum+1
		if(n1>0 and n2>0):
			filename=ss[0:n1]
			filename+=ss[n2:]
			print filename
			os.rename(ss, filename)
			changeNum=changeNum+1
	except ValueError:
		print "ValueError"
	except WindowsError:
		print "windows error"
	else:
		print "rename ok!"
print("fileNum:"+str(fileNum))
print("changeNum:"+str(changeNum))
