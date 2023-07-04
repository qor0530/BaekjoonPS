N, M, K = map(int,input().split())
tiles = []
for _ in range(N):
    tiles.append(list(input()))
ktile = [{} for _ in range(K*K)]
def tilecheck(x, y):
    for i in range(K):
        for j in range(K):
            try:
                ktile[i*K+j][tiles[x+i][y+j]] += 1
            except:
                ktile[i*K+j][tiles[x+i][y+j]] = 1
nk = N//K
mk = M//K
for i in range(nk):
    for j in range(mk):
        tilecheck(i*K, j*K)

string = ["" for i in range(K)]
count = 0
for i in range(K):
    for j in range(K):
        maxstring = max(ktile[i*K+j], key=ktile[i*K+j].get)
        count += (nk * mk) - ktile[i*K+j][maxstring]
        string[i] += maxstring
print(count)
for i in range(nk):
    for j in range(K):
        print(string[j]*mk)