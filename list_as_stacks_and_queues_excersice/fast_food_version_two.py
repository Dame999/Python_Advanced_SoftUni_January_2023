from collections import deque

food_quantity = int(input())
food_orders = deque([int(i) for i in input().split()])

print(max(food_orders))

for order in food_orders.copy():
    if food_quantity - order >= 0:
        food_orders.popleft()
        food_quantity -= order
    else:
        print(f"Orders left: {' '.join([str(o) for o in food_orders])}")
        break
else:
    print("Orders complete")
