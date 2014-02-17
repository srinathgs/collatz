import rmq
from datetime import datetime


class Collatz():
	"""
		This class takes in the maximum number upto which 
		the number of cycles required are to be calculated.
		This class generates the cycles in a bottom up fashion as
		this is a one time activity.
	"""
	def __init__(self, max_num = 1000000):
		print "Started building memoization table at",datetime.now()
		if max_num > 0:
			self.ctz_items = [-1 ] * (max_num + 1)
		else:
			raise Exception("Maximum Number should be greater than 0")
		self.size = max_num
		ctz = self.ctz_items
		ctz[1] = 1
		for i in xrange(1,max_num):
			j = i
			cycles = 0
			while j != 1 and j >= i:
				cycles += 1
				j = (j >> 1) if (j % 2 == 0) else (3 * j + 1)
			ctz[i] = cycles + ctz[j]
		print "End of table construction. Started building Segment Tree at", datetime.now()
		self.RMQ = rmq.RangeQuery(ctz, max, -1)
		print "End of Segment Tree construction", datetime.now()

	def size(self):
		return self.size

	def get_table(self):
		return self.ctz_items

	def get_item(self, number):
		return self.get_table()[number]

	def get_cycles(self,number):
		if number <= self.size:
			return self.get_item(number)
		else:
			return None
	def max_cycles(self, min_num, max_num):
		"""
			This function take O(n) to find the maximum number of cycles.
		"""
		if min_num > max_num:
			min_num, max_num = max_num, min_num
		max_val = -1
		ctz = self.get_table()
		for i in ctz[min_num:max_num + 1]:
			if i > max_val:
				max_val = i
		return max_val

	def max_cycles_r(self, min_num, max_num):
		"""
		This function uses Range Max Query to efficiently compute 
		the maximum number of cycles in the range asked.
		Takes O(log n) time to query using RMQ.
		"""
		if min_num > max_num:
			min_num, max_num = max_num, min_num
		max_val = -1
		return self.RMQ.query(min_num, max_num)
			
