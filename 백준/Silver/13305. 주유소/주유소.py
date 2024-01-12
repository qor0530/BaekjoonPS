N = int(input())
roads = list(map(int , input().split(' ')))
cities = list(map(int , input().split(' ')))

max_price = 0
road_len = 0
minimum_oil = cities[0]
for i in range(N-1):
    if minimum_oil > cities[i]:
        minimum_oil = cities[i]
    max_price += minimum_oil * roads[i]
print(max_price)
