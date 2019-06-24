from zipfile import ZipFile


#unzipped = zipf.read()

#print(unzipped)

#zipf.printdir()

def extract_files_from_zip():
	zipf = ZipFile('channel.zip', 'r')
	zipf.extractall(path='unzipped')


def follow_the_chain():
	n = '90052'

	while True:
		text = ''
		with open('unzipped/' + n + '.txt', 'r') as f:
			text = f.read()
		
		if text.find('Next nothing is') > -1:
			n = text.split()[-1]
		else:
			print(n)
			break


def extract_comments_from_zip_file():
	with open('channel.zip', 'rb') as f:
		for line in f.readlines():
			hl = line.find(b'#')
			if hl > -1:
				print_b_line(line[hl : ])


def print_b_line(line):
	for c in line:
		if c < 32 or c > 126:
			print('', end='')
		else:
			print(chr(c), end='')
	print()

#extract_comments_from_zip_file()

def extract_comments_from_zip_file_2():
	zipf = ZipFile('channel.zip', 'r')

	for zi in zipf.infolist():
		print(zi.comment.decode())#, end='')
	print()

extract_comments_from_zip_file_2()

