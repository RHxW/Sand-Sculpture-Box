


def IC(principal, i_rate, length):
    for arg in [principal, i_rate, length]:
        if type(arg) not in [int, float]:
            raise RuntimeError("args type error!")
    rate = 1 + i_rate
    res = principal * rate ** length
    return res

def ICR(principal, i_rate, length, step):
    for arg in [principal, i_rate, length, step]:
        if type(arg) not in [int, float]:
            raise RuntimeError("args type error!")
    length = int(length)
    rate = 1 + i_rate
    res = principal * rate
    for i in range(2, length+1):
        res = (res + step) * rate
        print(res)

    return res

