import math

n = int(input())
ring = []
ring = list(map(int, input().split()))

for _ in range(1, n):
  GCD = math.gcd(ring[0], ring[_])
  print(f'{int(ring[0]/GCD)}/{int(ring[_]/GCD)}')