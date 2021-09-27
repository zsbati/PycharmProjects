chicks = input().split(" ")
cows = []
for chick in chicks:
    if chick.endswith("s"):
        cows.append(chick)
print("_".join(cows))
