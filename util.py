import os
import requests

def loadfile(url, filename):
    '确保文件已经下载'
    if not os.path.isfile(filename):
        print('下载数据文件……')
        r = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(r.content)
        