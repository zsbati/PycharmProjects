prime_numbers = [2]
for i in range(3, 1000):
    if all(i % prime for prime in prime_numbers):
        prime_numbers.append(i)
#print(prime_numbers)
