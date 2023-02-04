from collections import deque

price_of_each_bullet = int(input())
size_of_the_gun_barrel = int(input())

bullets = deque(int(b) for b in input().split())

locks = deque(int(l) for l in input().split())

value_of_the_intelligence = int(input())

fired_bullets = 0
bullets_in_the_barrel = size_of_the_gun_barrel
while True:

    if len(locks) == 0:
        bullets_left = len(bullets)
        money_earned = value_of_the_intelligence - fired_bullets * price_of_each_bullet
        print(f"{bullets_left} bullets left. Earned ${money_earned}")
        break

    if len(bullets) == 0:
        locks_left = len(locks)
        print(f"Couldn't get through. Locks left: {locks_left}")
        break

    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    bullets_in_the_barrel -= 1
    fired_bullets += 1

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print("Ping!")

    if bullets_in_the_barrel == 0 and bullets:
        bullets_in_the_barrel = size_of_the_gun_barrel
        print("Reloading!")

