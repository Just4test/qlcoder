# http://www.qlcoder.com/task/75d8
import math
print(math.log(1024,2))
exit()
class Tail:
	'''
	组成地图的最小单位，8x8
	'''
	
	def __init__(self, map, data = None):
		if data is None:
			data = [[1 for i in range(8)] for j in range(8)]
		self.data = data
		
		self.map = map
		
		self.left = self.right = self.top = self.buttom = None
		self.lefttop = self.righttop = self.leftbuttom = self.rightbuttom = None
		
	def coord(self):
		return map.tailcoord(self)
		
		
	def __repr__(self):
		return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
	
	def get_v(self, x, y):
		tar = self
		if -1 == x:
			tar = self.left
			x = 7
		elif 8 == x:
			tar = self.right
			x = 0
		if -1 == y:
			tar = tar.top
			y = 7
		elif 8 == y:
			tar = tar.buttom
			y = 0
		return tar.data[x]
	
	def calc_to_cache(self):
		'计算生命的存亡变化并放入缓存'
		cache = [[False for i in range(8)] for j in range(8)]
		num = 0
		data = self.data
		for x in range(8):
			for y in range(8):
				
				l = 0
				if 0 == x:
					if self.left is not None:
						l = self.left[7][y]
				else:
					l = data[x - 1][y]
				
				r = 0	
				if 7 == x:
					if self.right is not None:
						r = self.right[0][y]
				else:
					r = data[x + 1][y]
						
				t = 0		
				if 0 == y:
					if self.top is not None:
						t = self.top[x][7]
				else:
					t = data[x][y - 1]
				
				b = 0
				if 7 == y:
					if self.buttom is not None:
						l = self.buttom[y][0]
				else:
					b = data[x][y] + 1
					
				temp = l + r + t + b
				
				if temp < 2 or temp > 3:
					result = 0
				elif 3 == temp:
					result = 1
				else:
					result = data[x][y]
					
				if result != data[x][y]:
					print('{} {} {}'.format(x, y, result))
				
				cache[x][y] = result
				num += result
				
		self.cache = cache
		self.cachenum = num
		
	def apply_cache(self):
		'应用缓存'
		self.data = self.cache
		self.num = self.cachenum
		self.cache = None
		
class QuadTree:
	'''
	四叉树，地图的支持数据结构。
	当deep大于0时，子节点是QuadTree。deep为0时，子节点是Tail
	'''
	
	def __init__(self, parrent = None):
		self.map = [[None, None], [None, None]]
		self.parrent = parrent
		
	def set_with_deep(self, tar, x, y, deep):
		if deep:
			_x = x >> deep
			_y = y >> deep
			if self.map[_x][_y] is None:
				self.map[_x][_y] = QuadTree()
				self.map[_x][_y].parrent = self
			self.map[_x][_y].set_with_deep(tar, x >> 1, y >> 1, deep - 1)
		else:
			#tar is Tail
			self.map[x][y] = tar
			tar.qtree = self
			
	def get_with_deep(self, x, y, deep):
		if deep:
			_x = x >> deep
			_y = y >> deep
			if self.map[_x][_y] is None:
				return None
			else:
				return self.map[_x][_y].get_with_deep(x >> 1, y >> 1, deep - 1)
				
class Map(QuadTree):
	'''
	地图。
	地图支持负坐标。支持自动扩容。支持查找地块
	'''
	
	def __init__(self):
		self.map = [[QuadTree(self), QuadTree(self)], [QuadTree(self), QuadTree(self)]]
		self.deep = 0
		
	def get(self, x, y):
		if int(math.log(x, 2)) > self.deep or int(math.log(y, 2)) > self.deep:
			return None
		_x = _y = 1
		if x < 0:
			_x = 0
			x = -x
		if y < 0:
			_y = 0
			y = -y
		tar = self.map[_x][_y]
		if tar:
			return tar.get_with_deep(x, y, self.deep)
		else:
			return None
			
	def set(self, tar, x, y):
		_x = _y = 1
		if x < 0:
			_x = 0
			x = -x
		if y < 0:
			_y = 0
			y = -y
			
		self.map[_x][_y].set_with_deep(tar, x, y, self.deep)
		
		
		
data = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]

t = Tail(data)
print(t)
t.calc_to_cache()
t.apply_cache()
print(t)