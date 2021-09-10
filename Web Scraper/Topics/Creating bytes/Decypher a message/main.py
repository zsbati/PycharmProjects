encoded_message = input()
key_number = int(input())

key_1, key_2 = key_number.to_bytes(2, byteorder='little')
new_key = key_1 + key_2
decoded_message = ''
for char in encoded_message:
    decoded_message += chr(ord(char) + new_key)
print(decoded_message)
