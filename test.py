import hisearch as module
import unittest

ITEMS = [dict(one=item[0], two=item[1]) for item in [(u"1",u"2"),
	(u"2",u"4"),
	(u"3",u"6")]]

class TestSingleElement(unittest.TestCase):
	def test_single_element_is_returned(self):
		item = dict(one=u"door", two=u"window")
		hs = module.HiSearch(items=[item])
		self.assertDictEqual(hs.search(dict(one=u"roof", two=u"floor"))[0]["item"], item)

class TestRepresentation(unittest.TestCase):
	def test_retrieve_as_set(self):
		hs = module.HiSearch(items=ITEMS)
		self.assertSetEqual(hs.items(), set(ITEMS))

	def test_unicode(self):
		pass

class TestConstructor(unittest.TestCase):
	def test_non_unicode_fails(self):
		def callable():
			hs = module.HiSearch(items = [dict(one=1)])
		self.assertRaises(Exception, callable)		

	def test_dicts_are_receieved(self):
		hs = module.HiSearch(items=ITEMS)

	def test_incompatible_dicts_fail(self):
		def callable():
			hs = module.HiSearch(items = [dict(one=u"1", two=u"2"), dict(one=u"3", two=u"4", three=u"5")])
		self.assertRaises(Exception, callable)

	def test_not_iterable_fails(self):
		def callable():
			hs = module.HiSearch(items=1)
		self.assertRaises(Exception, callable)

	def test_order_does_not_matter(self):
		hs1 = module.HiSearch(items=ITEMS)
		hs2 = module.HiSearch(items=ITEMS.sorted())
		self.assertSetEqual(hs1.items(), hs2.items())

class TestExactMatch(unittest.TestCase):
	def test_exact_match_of_all_parts(self):
		hs = module.HiSearch(items=[(u"door", u"window")])
		self.assertEqual(hs.search((u"door", u"window"))[0]["item"], (u"door", u"window"))

	def test_match_of_some_parts_is_not_exact(self):
		pass

class TestSearch(unittest.TestCase):
	def test_exact_match_is_exact(self):
		hs = module.HiSearch(items=[(u"door", u"window")])
		self.assertEqual(hs.search((u"door", u"window"))[0]["score"], 1.0)

	def test_all_items_returned(self):
		hs = module.HiSearch(items=ITEMS)
		found = [item["item"] for item in hs.search((u"1", u"2"))]
		self.assertSetEqual(set(found), set(ITEMS))

	def test_threshold_respected(self):
		hs = module.HiSearch(items=ITEMS)
		for threshold in range(10):
			found = [item["score"]>=threshold/10.0 for item in hs.search((u"1", u"2"), threshold=threshold/10.0)]
			self.failUnless(all(found))
		
	def test_results_ordered_by_score(self):
		hs = module.HiSearch(items=ITEMS)
		found = [item["score"] for item in hs.search((u"1", u"2"))]
		score = 1.0
		for element in found:
			self.failIf(element>score)
			score = element		

class TestKnownValues(unittest.TestCase):
	pass

if __name__ == '__main__':
    unittest.main()