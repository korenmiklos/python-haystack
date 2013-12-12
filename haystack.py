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

class HayStack(Needle):
	'''
	A HayStack is a collection of HayStacks or Needles. 
	'''
	def __init__(self, items, text=None):
		super(HayStack, self).__init__(text)
		self.items = set([])
		for item in items:
			if isinstance(item, basestring):
				self.items.add(Needle(item))
			elif isinstance(item, Needle):
				self.items.add(item)

	def search(self, list_of_text):
		if len(list_of_text)==0:
			return []
		if isinstance(list_of_text, basestring):
			list_of_text = [list_of_text]
		text = list_of_text[0]
		best_score = 0.0
		for item in self.items:
			new_score = item.matches(text)
			if new_score>=best_score:
				best_score = new_score
				found = item
		return [dict(item=found.text, score=best_score)]

