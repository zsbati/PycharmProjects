min_ = int(input())
max_ = int(input())
actual = int(input())
    
if actual < min_:
    print("Deficiency")
elif actual > max_:
    print("Excess")
else:
    print("Normal")
