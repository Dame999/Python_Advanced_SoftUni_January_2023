from collections import deque

chocolates = deque([int(i) for i in input().split(', ')])
cups_of_milk = deque([int(i) for i in input().split(', ')])

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:

    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolate -= 5
        chocolates.append(chocolate)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    chocolates = (str(i) for i in chocolates)
    print(f"Chocolate: {', '.join(chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    cups_of_milk = (str(i) for i in cups_of_milk)
    print(f"Milk: {', '.join(cups_of_milk)}")
else:
    print("Milk: empty")