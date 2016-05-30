# http://www.qlcoder.com/task/75ab

url = 'http://www.qlcoder.com/download/blowfish.data'
filename = 'temp_75ab.data'
password = 'qlcoder'
__import__('util').loadfile(url, filename)
from subprocess import *
args = 'openssl blowfish -d -in {} -pass "pass:{}"'.format(filename, password)
print(args)
__import__('os').system(args)