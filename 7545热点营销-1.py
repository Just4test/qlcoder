# http://www.qlcoder.com/task/7545
import os

filename = 'temp_7545.txt'
fileurl = 'http://qlcoder.com/download/144047638844506.txt'
if not os.path.isfile(filename):
	print('下载数据文件……')
	import requests
	r = requests.get(fileurl)
	with open(filename, 'wb') as f:
		f.write(r.content)
		
		
usernum = 100
f = open(filename)
users = [[i] for i in range(usernum)]

for line in f.readlines():
	temp = line.split(' ')
	a = int(temp[0]) - 1
	b = int(temp[1]) - 1
	if users[b] != users[a]:
		for k in users[b]:
			users[a].append(k)
			users[k] = users[a]
#	if a not in users and b not in users:
#		users[a] = users[b] = [a, b]
#	else:
#		if a not in users:
#			a, b = b, a
#		if b not in users:
#			users[a].append(b)
#			users[b] = users[a]
#		elif users[b] != users[a]:
#			for k in users[b]:
#				users[a].append(k)
#				users[k] = users[a]
	
count = 0
for i in range(usernum):
	if users[i] is not None and users[users[i][0]] is not None:
		print('圈子{}，长度{}'.format(users[i], len(users[i])))
		count += 1
		users[users[i][0]] = None
	
print('共有圈子{}个'.format(count))
		