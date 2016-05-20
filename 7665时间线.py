#!/usr/bin/python3
# http://www.qlcoder.com/task/7665

USER_TOTAL = 10000000

import math
import hashlib

users = []
class User:
    '单个用户'
    __slots__ = [
        'id',
        'hot', # 指示是否是网络红人。红人的消息读扩散，非红人的消息写扩散
        'following', # 关注的人
        'follower', # 关注自己的人。如果自己不是红人，则发的信息投递到follower的inbox中。
        'hotfollowing', # 关注的网络红人。需要从这些人的outbox中读取消息。每个元素是(id, outboxindex)
        'inbox', # 关注的人中非红人的更新投递到inbox
        'outbox', # 红人才有用，自己的更新列表
    ]
    
    def follow(self, id):
        tar = users[id - 1]
        self.following.append(tar)
        tar.follower.append(self)
        if tar.hot:
            self.hotfollowing.append([tar, 0])
    
    def __init__(self, id):
        self.id = id
        self.hot = False
        self.following = []
        self.follower = []
        self.hotfollowing = []
        self.inbox = []
        self.outbox = []
        
        # 填充关注列表
        if id == 1:
            self.following = users
            self.hot = True
        else:
            self.follow(1)
            to_value = int(__import__('math').sqrt(id))
            for i in range(2, to_value + 1):
                if id % i == 0:
                    self.follow(i)
                    if id / i != i:
                        self.follow(int(id / i))

    def post(self, msg):
        if self.hot:
            self.outbox.append(msg)
        else:
            for user in self.follower:
                user.inbox.append(msg)
                
    def view(self):
        temp = self.inbox
        self.inbox = []
        
        for data in self.hotfollowing:
            temp += data[0].outbox[data[1]:]
            data[1] = len(data[0].outbox)
        def getindex(msg):
            return msg[0]
        temp.sort(key = getindex)
        
        temp.reverse()
        temp = [msg[1] for msg in temp]
        return '-'.join(temp)

url = 'http://121.201.63.168/uploads/145813004658861.py'
filename = 'temp_7665.py'
DATA_FILE = 'temp_7665_data.txt'
__import__('util').loadfile(url, filename)

print('生成数据文件……')
import os
os.system('python {}'.format(filename))
os.rename('timeline.txt', DATA_FILE)

print('初始化用户……')
for i in range(1, USER_TOTAL + 1):
    users.append(User(i))
    if i % 100000 == 0:
        print('已处理{}万个用户'.format(int(i / 10000)))

print('处理行为……')
md5list = []
data = open(DATA_FILE)
lineindex = 0
for line in data:
    temp = line.split(' ')
    user = users[int(temp[1]) - 1]
    if temp[0] == 'p':
        msg = (lineindex, temp[2][:-1])
        user.post(msg)
    else:
        view = user.view()
        # print('"{}"'.format(view))
        md5 = hashlib.md5(view.encode())
        md5list.append(md5.hexdigest())
        
    lineindex += 1
    
    if lineindex % 100000 == 0:
        print('已处理{}万条记录'.format(int(lineindex / 10000)))
    
temp = '-'.join(md5list)
# print(temp)
md5 = hashlib.md5(temp.encode())
print('答案是', md5.hexdigest())
