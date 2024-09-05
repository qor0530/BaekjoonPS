a = input()
boards = list()
string = ""
for i in range(len(a)):
    if a[i] == ".":
        boards.append(string)
        boards.append(".")
        string = ""
    else:
        string += a[i]
        if i == len(a) - 1:
            boards.append(string)
result = ""
for board in boards:
    if board == ".":
        result += "."
    else:
        length = len(board)
        while(length > 0):
            if length >= 4:
                result += "AAAA"
                length -= 4
            elif length >= 2:
                result += "BB"
                length -= 2
            else:
                result = "-1"
                break
    if result == "-1":
        break
print(result)
