from collections import deque

parentheses = deque(input())
opening_parentheses = deque()

for i in range(len(parentheses)):

    cur_parenthesis = parentheses.popleft()

    if cur_parenthesis in "{[(":
        opening_parentheses.append(cur_parenthesis)
    else:
        if not opening_parentheses:
            print("NO")
            break
        else:
            last_open_parenthesis = opening_parentheses.pop()

            if f"{last_open_parenthesis + cur_parenthesis}" in "{}[]()":
                continue
            else:
                print("NO")
                break
else:
    print("YES")

