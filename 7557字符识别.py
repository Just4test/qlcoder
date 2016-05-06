# 安装7z: sudo apt-get install p7zip
# 安装 PIL:
# sudo pip3 install pillow
# 安装tesseract（ocr库）：
# sudo apt-get install tesseract-ocr
# 安装 pytesseract ：
# sudo pip3 install pytesseract

import zipfile
import os
dirname = 'temp_752a'
filename = dirname + '.7z'
fileurl = 'http://qlcoder.com/download/cap1.7z'
if not os.path.isdir(dirname):
    if not os.path.isfile(filename):
        print('下载数据文件……')
        import requests
        r = requests.get(fileurl)
        with open(filename, 'wb') as f:
            f.write(r.content)
    print('解压缩……')
    os.system( '7zr x {} -o{}'.format(filename, dirname))
    print('数据准备完毕。')
    

from PIL import Image
import pytesseract
image = Image.open(dirname + '/cap1/im12.png')
print(pytesseract.image_to_string(image))