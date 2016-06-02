# http://www.qlcoder.com/task/7617

import os
import struct

url = 'http://121.201.63.168/uploads/145303100168558.png'
filename = 'temp_7617_source.png'
newfilename = 'temp_7617_target.png'
__import__('util').loadfile(url, filename)

from PIL import Image

image = Image.open(filename)
cache = image.load()

rows, cols = image.size
for i in range(rows):
    for j in range(cols):
        cache[i,j] = ((cache[i, j][0] & 1) << 8, 0, 0)

image.save(newfilename)