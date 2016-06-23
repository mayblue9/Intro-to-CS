def bad_hash_string(keyword, buckets):
	return ord(keyword[0]) % buckets

def test_hash_function(func, keys, size):
	results = [0] * size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv = func(w,size)
			results[hv] += 1
			keys_used.append(w)
	return results

print(test_hash_function(bad_hash_string, '', 5))