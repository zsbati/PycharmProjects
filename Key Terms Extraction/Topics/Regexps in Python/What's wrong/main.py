import re

w_1 = input()
w_2 = input()
if re.match(w_1, w_2) is not None:
    print(len(w_1) * 2)
else:
    print('no matching')
