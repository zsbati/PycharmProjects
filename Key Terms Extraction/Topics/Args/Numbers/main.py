# put your python code here
def multiply(*args):
    if len(list(args)) == 1:
        return list(args)[0]
    product = 1
    for n in list(args):
        product *= n
    return product
