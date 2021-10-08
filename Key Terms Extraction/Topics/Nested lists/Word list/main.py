text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

max_length = int(input())

output = []

for sentence in text:
    for word in sentence:
        if len(word) <= max_length:
            output.append(word)

print(output)
