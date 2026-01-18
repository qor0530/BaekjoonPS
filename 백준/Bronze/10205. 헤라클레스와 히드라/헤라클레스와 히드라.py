n = int(input())
for i in range(n):
    h = int(input())
    string = input()
    for j in range(len(string)):
        if string[j] == "c":
            h += 1
        if string[j] == "b":
            h -= 1
    print(f"Data Set {i+1}:\n{h}\n")
