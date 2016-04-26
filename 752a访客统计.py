# http://www.qlcoder.com/task/752a

import os

filename = 'temp_752a.txt'
fileurl = 'http://www.qlcoder.com//download/uv.txt'
if not os.path.isfile(filename):
	print('下载数据文件……')
	import requests
	r = requests.get(fileurl)
	with open(filename, 'wb') as f:
		f.write(r.content)
		
f = open(filename)
iddic = {}
cont = 0
for line in f.readlines():
	temp = line.split(' ')
	id = temp[1]
	if id not in iddic:
		iddic[id] = True
		cont += 1
print('访客数{}'.format(cont))
	