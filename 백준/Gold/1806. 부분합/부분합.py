n, s = map(int, input().split())

seq = list(map(int, input().split()))

now = seq[0]
start = 0
end = 0
min_length = 100001
while True:
    if now <= s:
        if now == s:
            length = end - start + 1
            if min_length > length:
                min_length = length
        end += 1
        if end != n:
            now += seq[end]
        else:
            break
    else:
        length = end - start + 1
        if min_length > length:
            min_length = length
        now -= seq[start]
        start += 1
    # print(start, end, now)
if min_length != 100001:
    print(min_length)
else:
    print(0)