class HiSearch(object):
	'''
	Search an element within a set. Each element is a tuple (of arbitrary length)
	 (a, b, c, d)
	and the assumption is that earlier parts of the tuple are less likely to be misspelled.

	Example:
	 (state, county, city)
	so that
	 (NJ, Mercer, Princton)
	matches
	 (NJ, Mercer, Princeton)
	'''

	def __init__(self, items):
		length = len(items[0])
		for item in items:
			if not len(item)==length:
				raise Exception
			for part in item:
				assert isinstance(part, unicode)
		self._items = set(items)

	def search(self, tuple):
		if tuple in self.items():
			return [dict(item=tuple, score=1.0)]
		else:
			return [dict(item=list(self.items())[0], score=0.0)]

	def items(self):
		return self._items