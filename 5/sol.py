import urllib.request
import sys

done = False
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
n = 12345 if len(sys.argv) < 2 else int(sys.argv[1])
c = 1
logf = open('req.log', 'w')

while not done:
	url = base_url + str(n)
	print(c, ". fetching ", url)
	logf.write(str(c) + ". get " + url + '\n')
	logf.flush()
	c += 1
	if c > 400:
		print(url)
		break

	with urllib.request.urlopen(url) as r:
		text = r.read()
		if text.find(b"and the next nothing is") == -1:
			print(url)
			if n == 16044:
				n = int(n / 2)
				continue
			if n == 66831:
				n = "peak.html"
				continue
			break
		n = int(text.split()[-1])

logf.close()
