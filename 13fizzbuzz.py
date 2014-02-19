from sys import argv

for i in range(1,int(argv[1])+1):
	if 0 == i % 15:
		print 'FIZZBUZZ'
	elif 0 == i % 5:
		print 'BUZZ'
	elif 0 == i % 3:
		print 'FIZZ'
	else:
		print i