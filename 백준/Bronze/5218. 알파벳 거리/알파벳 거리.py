n = int(input())

for i in range(n):
    a, b = input().split()
    a_list = []
    b_list = []
    for alpha in a:
        a_list.append(ord(alpha) - 64)
    for beta in b:
        b_list.append(ord(beta) - 64)
    print(f"Distances: ", end="")
    for count in range(len(a_list)):
        if a_list[count] <= b_list[count]:
            print(f"{b_list[count] - a_list[count]} ", end="")
        else:
            print(f"{26 - a_list[count] + b_list[count]} ", end="")
    print()