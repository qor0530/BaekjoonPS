N = int(input())

for i in range(N):
    R, S = input().split()
    R = int(R)
    n_str = ""
    for j in range(len(S)):
        n_str += S[j] * R
    print(n_str)