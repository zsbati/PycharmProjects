t = int(input().strip())  # number of test cases
A = set(map(int, input().split()))  # set A to be examined
for i in range(t):
    sB = int(input())
    B = set(map(int, input().split()))
    print(B.issubset(A))
