"""
def ssort(somelist):
    i = 0
    for x in somelist[i:]:
        for y in somelist[i:]:
            if y > x:
                num = y + 0
                x = y
                y = num
        somelist[i] = y
        print(somelist)
        i += 1


"""
def ssort(somelist):
    i = 0
    while i < len(somelist):
        smallest = somelist[-1]
        smallest_in = len(somelist) - 1
        for x in range(i,len(somelist)):
            if somelist[x] < smallest:
                smallest = somelist[x]
                smallest_in = x
        num = somelist[i]
        somelist[i] = smallest
        somelist[smallest_in] = num
        print(somelist)
        i += 1



testList = [3, 5, 2, 8, 9, 1]
ssort(testList)
