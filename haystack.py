class Needle(object):
	'''
	A needle contains a string and can respond to string comparisons.
	'''
	def __init__(self, text):
		self.text = text

	def matches(self, other):
		if self.text==other:
			return 1.0
		else:
			return 0.0

class HayStack(object):
	'''
	A HayStack is a collection of HayStacks or Needles. 
	'''
	def __init__(self, items):
		self.items = set([])
		for item in items:
			if isinstance(item, basestring):
				self.items.add(Needle(item))
			elif isinstance(item, Needle):
				self.items.add(item)

	def search(self, list_of_text):
		pass
