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

class TestSearch(unittest.TestCase):
	def setUp(self):
		needles = [u"quick brown fox", u"árvíztűrő tükörfúrógép"]
		self.hs = haystack.HayStack(items=needles)

	def test_empty_list_fails_gracefully(self):
		self.assertListEqual(self.hs.search([]), [])

	def test_text_passed_to_search(self):
		found1 = self.hs.search("quick")[0]
		found2 = self.hs.search(["quick"])[0]
		self.assertDictEqual(found1, found2)

	def test_single_item_found(self):
		hs = haystack.HayStack(items=["abcd e"])
		self.assertEqual(hs.search("abcd e")[0]["item"], "abcd e")

	def test_exact_match_is_one(self):
		results = self.hs.search(u"quick brown fox")
		self.assertEqual(results[0]["score"], 1.0)

	def test_score_same_for_needle(self):
		needle = haystack.Needle("brown fox")
		hs = haystack.HayStack(items=[needle])
		self.assertEqual(hs.search("blue fox")[0]["score"], needle.matches("blue fox"))

class TestKnownValues(unittest.TestCase):
	pass

if __name__ == '__main__':
    unittest.main()