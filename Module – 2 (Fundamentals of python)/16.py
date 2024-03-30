
a="the quick brown fox jumps over the lazy dog."
b=a.split()
print (dict((c,b.count(c))for c in b))
