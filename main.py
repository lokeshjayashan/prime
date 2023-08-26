while True:
	def factors(n):
		faclist = []
		for i in range(1, n + 1):
			if n % i == 0:
				faclist += [i]
		return (faclist)
	def isprime(n):
		return (factors(n) == [1, n])
	def primeto(n):
		primelist = []
		for i in range(1, n + 1):
			if isprime(i):
				primelist += [i]
		return (primelist)
	def nprime(n):
		(c, i, plist) = (0, 1, [])
		while (c < n):
			if isprime(i):
				(c, plist) = (c + 1, plist + [i])
			i = i + 1
		return (plist)
	z = int(input("enter value\n"))
	print(z, "is prime :", isprime(z))
	print("factors of", z, ":", factors(z))
	print("prime numbers from 1 to", z, ":", primeto(z))
	print("first", z, "prime numbers :", nprime(z))