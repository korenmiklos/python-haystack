import hisearch as module
import unittest

ITEMS = [(u"1",u"2"),
	(u"2",u"4"),
	(u"3",u"6")]

class TestSingleElement(unittest.TestCase):
	def test_single_element_is_returned(self):
		hs = module.HiSearch(items=[(u"door", u"window")])
		self.assertItemsEqual(hs.search((u"roof", u"floor"))[0]["item"], (u"door", u"window"))

class TestRepresentation(unittest.TestCase):
	def test_retrieve_as_set(self):
		hs = module.HiSearch(items=ITEMS)
		self.assertSetEqual(hs.items(), set(ITEMS))

	def test_unicode(self):
		pass

class TestConstructor(unittest.TestCase):
	def test_non_unicode_fails(self):
		def callable():
			hs = module.HiSearch(items = [(1, 2), (2, 3)])
		self.assertRaises(Exception, callable)		

	def test_tuples_are_receieved(self):
		hs = module.HiSearch(items=ITEMS)

	def test_incompatible_tuples_fail(self):
		def callable():
			hs = module.HiSearch(items = [(u"1",u"2"), (u"3",u"4",u"5")])
		self.assertRaises(Exception, callable)

	def test_singleton_converted_to_tuples(self):
		hs = module.HiSearch(items=[u"1",u"2"])
		self.assertSetEqual(hs.items(), set([(u"1"), (u"2")]))

	def test_not_iterable_fails(self):
		def callable():
			hs = module.HiSearch(items=1)
		self.assertRaises(Exception, callable)

	def test_order_does_not_matter(self):
		hs1 = module.HiSearch(items=
			[(u"1",u"2"),
			(u"2",u"4"),
			(u"3",u"6")])
		hs2 = module.HiSearch(items=
			[(u"1",u"2"),
			(u"3",u"6"),
			(u"2",u"4")])
		self.assertSetEqual(hs1.items(), hs2.items())

class TestExactMatch(unittest.TestCase):
	def test_exact_match_of_all_parts(self):
		hs = module.HiSearch(items=[(u"door", u"window")])
		self.assertItemsEqual(hs.search((u"door", u"window"))[0]["item"], (u"door", u"window"))

	def test_exact_match_is_exact(self):
		pass

	def test_match_of_some_parts_is_not_exact(self):
		pass

class TestKnownValues(unittest.TestCase):
	pass

if __name__ == '__main__':
    unittest.main()