import os
import sys
s1='-'
s2='.'
filename=''
fileNum=0
changeNum=0
dir=sys.argv[1]
for ss in os.listdir(dir):
	print ss
	try:
		n1=ss.index(s1)
		n2=ss.index(s2)
		fileNum=fileNum+1
		if(n1>0 and n2>0):
			filename=ss[0:n1]
			filename+=ss[n2:]
			print filename
			os.rename(ss, filename)
			changeNum=changeNum+1
	except ValueError:
		print "ValueError"
	else:
		print "rename ok"
print("fileNum:"+str(fileNum))
print("changeNum:"+str(changeNum))