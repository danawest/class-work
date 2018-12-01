cats = ['girl cat', 'stripey', 'little cat', 'stella', 'fiona', 'locksley']
print(cats)
print(cats[-2])
message = "My last cat was called " + cats[-2].title() + "."
print(message)
cats.insert(0, 'starlight')
print(cats)
cats.append('samantha')
print(cats)
del cats[-1]
print(cats)
first_cat = cats.pop(0)
message = "The first cat I named was called " + first_cat.title() + "."
print(message)
print(cats)
ran_away = 'stella'
cats.remove(ran_away)
print(cats)
print("My cat " + ran_away.title() + " ran away in 2005.")
print(sorted(cats))
print(sorted(cats,reverse=True))
print(cats)
cats.reverse()
print(cats)
print(len(cats))