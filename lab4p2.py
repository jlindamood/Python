def emul(a, b):
    resultSum = 0

    sign = 1
    if a > 0 and b > 0:
        sign = 1
    if a > 0 and b < 0:
        sign = -1
        b = -b
    if a < 0 and b > 0:
        sign = -1
        a = -a
    if a < 0 and b < 0:
        sign = 1
        a = -a
        b = -b

    while b > 0:
        if b % 2 == 1:
            resultSum += a
        a = a*2
        b = b//2

    if sign == -1:
        resultSum = resultSum - 2 * resultSum
    print(resultSum)
    return resultSum

emul(22, 21)
emul(-22, 21)
emul(-22, -21)
