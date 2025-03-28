def appendAtFront(x,L):
    return [x + element for element in L]

def bitStrings(n):
    if n==0:
        return []
    elif n==1:
        return ['0', '1']
    else:
        return (appendAtFront('0', bitStrings(n-1)) + appendAtFront('1', bitStrings(n-1)))

print(bitStrings(4))

def bitStrings(n):
    if n == 0:
        return []
    elif n == 1:
        return ['0', '1']
    else:
        return [digit + bitstring for digit in bitStrings(1)
                            for bitstring in bitStrings(n-1)]

print(bitStrings(4))