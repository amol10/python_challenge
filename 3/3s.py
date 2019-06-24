import re

'''
html = ''

with open('ocr.html', 'rb') as f:
	html = f.read()

c = 0
block = ''
block_start = False

for line in html.splitlines():
	print(line)
	input()
	if line.strip() == b"-->":
		block_start = False

	if block_start:
		block += line.strip()

	if line.strip() == b"<!--":
		if c == 1:
			block_start = True
		else:
			c += 1

print(block)
'''

block = b''

with open('ocr_block.txt', 'rb') as f:
	block += f.read()

map = {}

for c in block:
	if not c in map.keys():
		map[c] = 1
	else:
		map[c] += 1

print(map)

t = []
for (c, f) in map.items():
	t.append((chr(c), f))

print(t)

st = sorted(t, key=lambda x: x[1])#, reverse=True)

print(st)
print()

for (c, f) in st:
	print(c, ": ", f)
