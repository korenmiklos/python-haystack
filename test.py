# -*- coding: utf-8 -*-
import haystack
import unittest

class TestNeedle(unittest.TestCase):
	def setUp(self):
		self.simple_needle = haystack.Needle("quick brown fox")
		self.unicode_needle = haystack.Needle(u"árvíztűrő tükörfúrógép")

	def test_needle_matches_itself(self):
		self.assertEqual(self.simple_needle.matches(self.simple_needle.text), 1.0)

	def test_simple_needle_matches_text(self):
		self.assertEqual(self.simple_needle.matches("quick brown fox"), 1.0)

	def test_unicode_needle_matches_text(self):
		self.assertEqual(self.unicode_needle.matches(u"árvíztűrő tükörfúrógép"), 1.0)

	def test_imperfect_accent_match(self):
		self.failIf(self.simple_needle.matches(u"arvizturo tukorfurogep")==1.0)

class TestHayStack(unittest.TestCase):
	def test_items_is_set(self):
		needle1 = haystack.Needle("quick brown fox")
		needle2 = haystack.Needle(u"árvíztűrő tükörfúrógép")
		hs = haystack.HayStack(items=[needle1, needle2])
		self.failUnless(isinstance(hs.items, set))

	def test_construction_from_needles(self):
		needle1 = haystack.Needle("quick brown fox")
		needle2 = haystack.Needle(u"árvíztűrő tükörfúrógép")
		hs = haystack.HayStack(items=[needle1, needle2])
		self.assertSetEqual(hs.items, set([needle1, needle2]))

	def test_construction_from_texts(self):
		needles = ["quick brown fox", u"árvíztűrő tükörfúrógép"]
		hs = haystack.HayStack(items=needles)
		for item, text in zip(hs.items, needles):
			self.assertEqual(item.text, text)

	def test_construction_from_mixed(self):
		needles = [haystack.Needle("quick brown fox"), u"árvíztűrő tükörfúrógép"]
		hs = haystack.HayStack(items=needles)
		self.assertSetEqual(set([item.text for item in hs.items]), set(["quick brown fox", u"árvíztűrő tükörfúrógép"]))

class TestKnownValues(unittest.TestCase):
	pass

if __name__ == '__main__':
    unittest.main()