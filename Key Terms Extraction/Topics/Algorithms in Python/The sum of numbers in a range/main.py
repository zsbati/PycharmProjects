def range_sum(numbers, start, end):
    out = 0
    for number in numbers:
        if start <= number <= end:
            out += number
    return out        

input_numbers = [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]
print(range_sum(input_numbers, a, b))
