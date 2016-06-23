def hash_string(keyword, buckets):
	t = 0
	for c in keyword:
		t += ord(c)
	return t % buckets

def test_hash_function(func, keys, size):
	results = [0] * size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv = func(w,size)
			results[hv] += 1
			keys_used.append(w)
	return results

test_string = 'The quick brown fox jumped over the lazy dogs'


print(hash_string('udacity',12))
print(test_hash_function(hash_string, 'udacity',12))
print(hash_string('a',12))
#>>> 1

print(hash_string('b',12))
#>>> 2

print(hash_string('a',13))
#>>> 6

print(hash_string('au',12))
#>>> 10

print(hash_string('udacity',12))
#>>> 11
