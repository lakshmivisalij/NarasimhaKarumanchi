def printFunc(n):
    if n==0:
        return 0
    else:
        print(n)
        printFunc(n-1)


printFunc(4)

