clothes = [int(n) for n in input().split()]
rack_capacity = int(input())
current_rack_capacity = rack_capacity
racks_counter = 1
for i in range(len(clothes)):

    current_cloth = clothes.pop()
    if current_rack_capacity - current_cloth >= 0:
        current_rack_capacity -= current_cloth
    else:
        racks_counter += 1
        current_rack_capacity = rack_capacity - current_cloth

print(racks_counter)
