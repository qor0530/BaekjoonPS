import sys
sys.setrecursionlimit(10**7)

n, r, c = map(int, input().split())

count = [0]
def z(n, x, y):
    if n == 0:
        if x == r and y == c:
            print(count[0])
            exit()
        count[0] += 1
    else:
        for a, b in [(0,0),(0,2**(n-1)),(2**(n-1),0),(2**(n-1),2**(n-1))]:
            ax, by = x+a, y+b
            if ax <= r <= ax+2**(n-1)-1 and by <= c <= by+2**(n-1)-1:
                z(n-1, x+a, y+b)
                break
            else:
                count[0] += (2**(n-1))**2
z(n, 0, 0)