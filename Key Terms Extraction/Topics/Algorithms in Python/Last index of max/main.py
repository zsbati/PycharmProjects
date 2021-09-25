def last_indexof_max(numbers):
    # write the modified algorithm here
    numbers.reverse()
    return len(numbers) - numbers.index(max(numbers)) - 1
