def mul(a, b):
    if a == 0 or b == 0:
        return 0

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

    if a < b:
        counter = a - 1
    else:
        counter = b - 1

    result = a
    while (counter > 0):
        result = a + a
        counter -= 1

    if sign == -1:
        result = result - result - result
    print(result)
    return result

mul(2, 1)
mul(4, 2)
mul(8, 2)
mul(-2, -2)
mul(-2, 2)
