def Division(val):
    val = tuple(val)
    res = val[0]
    for i in val[1:]:
        if i == 0:
            return 'Cannot Divide by 0'
        res /= i
    return res


def floor_division(val):
    val = tuple(val)
    res = val[0]
    for i in val[1:]:
        if i == 0:
            return 'Cannot Divide by 0'
        res //= i
    return res


def modulous(val):
    val = tuple(val)
    res = val[0]
    for i in val[1:]:
        if i == 0:
            return 'Cannot Divide by 0'
        res %= i
    return res


def Division_Operation():
    choose = input('Enter Division Operations from /,//,% : ')
    if choose == '/':
        val = map(int, input('Enter Numbers to divide: ').split())
        return Division(val)
    elif choose == '//':
        val = map(int, input('Enter Numbers to divide: ').split())
        return floor_division(val)
    elif choose == '%':
        val = map(int, input('Enter Numbers to divide: ').split())
        return modulous(val)
    else:
        print('choose Correct Division Operations')
        return Division_Operation(val)
