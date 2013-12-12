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

	def __init__(self, items, hierarchy):
		pass

	def search(self, dct, thresholds=[]):
		if not thresholds:
			thresholds = [0.0]*len(dct)
		found = self._ngram.search(stringify(tuple), threshold=thresholds[0])
		return [dict(item=destringify(item[0]), score=item[1]) for item in found]

	def items(self):
		pass

class Needle(object):
	'''
	A needle contains a string and can respond to string comparisons.
	'''
	def __init__(self, text):
		pass

	def matches(self, other):
		pass

class HayStack(object):
	'''
	A HayStack is a collection of HayStacks or Needles. 
	'''
	def __init__(self, items):
		pass

	def search(self, list_of_text):
		pass
