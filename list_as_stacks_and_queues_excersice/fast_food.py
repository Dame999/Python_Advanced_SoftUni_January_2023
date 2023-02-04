from collections import deque

quantity_of_the_food = int(input())
orders = input().split()
int_orders = deque()
for item in orders:
    int_orders.append(int(item))

print(max(int_orders))

for i in range(len(orders)):
    if orders:
        current_order = int_orders[0]
        if current_order <= quantity_of_the_food:
            int_orders.popleft()
            quantity_of_the_food -= current_order
        else:
            break
if int_orders:

    print(f"Orders left: ", end="")
    print(*int_orders, sep=", ")

else:
    print("Orders complete")
