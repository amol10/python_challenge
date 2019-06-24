import pickle

out = None
with open('banner.pickle', 'rb') as f:
	out = pickle.load(f)

for a in out:
	for e in a:
		print(e[0]*e[1], end='')
	print('')

