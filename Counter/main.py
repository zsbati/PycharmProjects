from collections import Counter

profit = 0

num_shoes = int(input())

stri = input()
arr = stri.split()

li = []
for i in range(len(arr)):
    li.append(int(arr[i]))
counts = Counter(li)

#print(counts)

customers = int(input())
for i in range(customers):
    stri = input()
    arr = stri.split()
    size = int(arr[0])
    #print('size')
    #print(size)
    price = int(arr[1])
    #print('quant of the size')
    quant = counts[size]
    #print(quant)
    if quant > 0:
        #print('entered')
        quant = quant - 1
        counts[size] = quant
        profit = profit + price
        #print(profit)
        #print(counts[size])
print(profit)
