def somar():
    count = 0
    print ('count-s', count)
    count += 2
    def inner():
        nonlocal count
        count += 1
        return count
    print('count-s2', count)
    return inner()
print(somar())
