import re

block = ''

with open('equality_block.txt', 'r') as f:
	block = ''.join(f.read().splitlines())

matches = re.compile("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]").findall(block)

r = ''.join(map(lambda s: s[4], matches))
print(r)
