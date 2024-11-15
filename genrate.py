def m (x, y):
    while x<=y:
        yield x
        x+=1

        g= m(5, 10)
        for y in g:
            print(y)
