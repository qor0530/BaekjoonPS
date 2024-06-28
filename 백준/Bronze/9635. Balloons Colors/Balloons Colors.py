T = int(input())
for i in range(T):
    case = list(map(int, input().split()))
    N = case[0]
    easy = case[1]
    hard = case[2]
    
    isEasy = False
    isHard = False
    problem = list(map(int, input().split()))
    if problem[0] == easy:
        isEasy = True
    if problem[-1] == hard:
        isHard = True
    if isEasy and isHard:
        print("BOTH")
    elif isEasy:
        print("EASY")
    elif isHard:
        print("HARD")
    else:
        print("OKAY")