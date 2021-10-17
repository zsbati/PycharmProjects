class NegativeSumError(BaseException):
    pass


def sum_with_exceptions(a, b):
    sum_ = a + b
    if sum_ < 0:
        raise NegativeSumError
    else:
        return sum_

'''try
    print(sum_with_exceptions(1, -2))
except NegativeSumError:
    print('error')'''
