list = [2,3,4,4,5,6,1,2,2,2,1,8,2]
def emerald(N):
    sum = 0
    store = 0
    num = 0
    for i in range(0, N):
        if list[i] % 2 == 0:
            sum += list[i]
        if list[i] % 2 != 0:
            store = sum
            sum = 0
        if num < store:
            num = store
    if num < sum:
        num = sum
    print(num)
emerald(13)
    