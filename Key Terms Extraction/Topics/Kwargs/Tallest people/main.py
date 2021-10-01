def tallest_people(**kwargs):
    max_ = max(kwargs.values())
    lst = [key for key in kwargs if max_ == kwargs.get(key)]
    lst.sort()
    for name in lst:
        print(name, ':', str(max_))
