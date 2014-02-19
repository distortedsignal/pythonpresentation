for i in range(1,101):
	if 0 == i % 15:
		print i, 'FIZZBUZZ'
	elif 0 == i % 5:
		print i, 'BUZZ'
	elif 0 == i % 3:
		print i, 'FIZZ'
	else:
		print i, i