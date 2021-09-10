number = int(input())
number_to_bytes = number.to_bytes(2, byteorder='little')
print(number_to_bytes[0] + number_to_bytes[1])
