n = int(input())
if n < 1:
    print("no army")
elif 1 <= n <= 9:
    print("few")
elif 10 <= n <= 49:
    print("pack")
elif 50 <= n <= 499:
    print("horde")    
elif 50 <= n <= 999:
    print("swarm")
elif n >= 1000:
    print("legion")
else:
    print("there is no such a case")
