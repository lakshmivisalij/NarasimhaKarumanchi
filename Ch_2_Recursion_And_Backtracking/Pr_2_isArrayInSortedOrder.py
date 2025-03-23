def isArrayInSortedOrder(A):
    if len(A)==1:
        return True
    return A[0] < A[1] and isArrayInSortedOrder(A[1:])

A = [12,23,45,76,90,120]
print(isArrayInSortedOrder(A))

