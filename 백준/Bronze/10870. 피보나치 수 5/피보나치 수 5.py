def pibo(a):
    if(a == 1):
        return 1
    elif(a == 0):
        return 0
    else:
        return pibo(a-1) + pibo(a-2)


N = int(input())
q = pibo(N)
print(q)
