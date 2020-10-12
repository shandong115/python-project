# -*- coding: UTF-8 -*-
import sys, os

#只读方式打开.srt文件
#只读方式打开doc.txt文件
#只写方式打开a.srt

#循环读取.srt文件，逐条处理

f_srt = sys.argv[1]
f_doc = sys.argv[2]
f_a_srt = 'a.srt'
with open(f_srt, 'r', encoding='utf-8') as fp_srt:
	with open(f_doc, 'r', encoding='utf-8') as fp_doc:
		content = fp_doc.read()
		start = 0
		end = 0
		with open(f_a_srt, 'w', encoding='utf-8') as fp_a_srt:
			while True:
				line = fp_srt.readline()
				if not line:
					break #已读到文件末尾
				try:
					if (line == '\n') or (len(line)>2 and line[2] == ':') or int(line) >=0:
						fp_a_srt.write(line) #回车空换行、时间、序列号直接写到新文件
				except ValueError:
					#fp_a_srt.write("这是内容"+"\r")
					#fp_a_srt.write()
					#length = len(line)
					#str_tmp = content[start: start+length-1]
					#if line[:length-2] == str_tmp:
						#start = start + length - 1
						#fp_a_srt.write(line)