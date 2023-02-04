from collections import deque

green_window = int(input())
free_window = int(input())
total_cars = 0
cars = deque()
command = input()
crash_happened = False
while command != "END":

    if command != "green":
        cars.append(command)
    else:
        current_green = green_window

        while 0 < current_green and cars:
            car = cars.popleft()

            time = current_green + free_window

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                crash_happened = True
                break

            current_green -= len(car)
            total_cars += 1
    if crash_happened:
        break
    command = input()

if not crash_happened:
    print("Everyone is safe.")
    print(f"{total_cars} total cars passed the crossroads.")
