def fizzbuzz(n):
# we will store the resulting numbers within an array
	result = []
	# loop from 1 to n
	for i in range(1, n + 1):
		add = ''
		# check if there is a remainder when dividing by 3, if not
		# then we know this number is divisible by 3
		if i % 5 == 0:
			add += 'Fizz'
		# check if divisible by 5
		if i % 9 == 0:
			add += 'Buzz'
			# not divisible by either 3 or 5
		if add == '':
			result.append(i)
		else:
			result.append(add)
	print(result)
fizzbuzz(100)