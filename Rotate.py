# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
	m = (ord(letter) + n - 96) % 26
	if m < 1:
		return chr(m + 122)
	else:
		return chr(m + 96)

def rotate(input, n):
	result = ''
	for c in input:
		if ord(c) < 97 or ord(c) > 122:
			result += c
		else:
			result += shift_n_letters(c, n)
	return result

print(rotate ('sarah', 13))
#>>> 'fnenu'
print(rotate('fnenu',13))
#>>> 'sarah'
print(rotate('dave',5))
#>>>'ifaj'
print(rotate('ifaj',-5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???
print(rotate("a",1))