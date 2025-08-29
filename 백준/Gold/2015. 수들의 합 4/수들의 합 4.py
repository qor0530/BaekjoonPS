from collections import defaultdict

n, k = map(int, input().split())
q = list(map(int, input().split()))

count = 0
prefix_sum = 0
freq = defaultdict(int)
freq[0] = 1  # 누적합 0이 한 번 등장(빈 구간)

for num in q:
    prefix_sum += num
    count += freq[prefix_sum - k]  # (현재 누적합 - k)가 이전에 등장했으면 카운트 증가
    freq[prefix_sum] += 1  # 현재 누적합 등장 횟수 갱신

print(count)
