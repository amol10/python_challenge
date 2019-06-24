st = input()
pt = ''

for c in st:
	if not c in ' .()yz':
		pt += chr(ord(c) + 2)
	elif c == 'y':
 		pt += 'a'
	elif c == 'z':
		pt += 'b'
	else:
		pt += c

print(pt)
