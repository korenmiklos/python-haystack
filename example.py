from haystack import HayStack

firms = [dict(name="BKV", city="Budapest"), dict(name="BKK", city="Budapest")]

hs = HayStack(items=firms, hierarchy=["city", "name"])

candidate = dict(name="BKV", city=None)
found = hs.search(candidate)
print found[0]["item"], found[0]["score"]
