n_number = int(input())

odd_nums = set()
even_nums = set()

for num in range(1, n_number + 1):
    name = input()
    current_sum_of_name_characters = sum([ord(ch) for ch in name]) // num

    if current_sum_of_name_characters % 2 == 0:
        even_nums.add(current_sum_of_name_characters)
    else:
        odd_nums.add(current_sum_of_name_characters)

if sum(odd_nums) == sum(even_nums):
    result = odd_nums.union(even_nums)
    result = [str(el) for el in result]
    print(f"{', '.join(result)}")

elif sum(odd_nums) > sum(even_nums):
    result = odd_nums.difference(even_nums)
    result = [str(el) for el in result]
    print(f"{', '.join(result)}")

elif sum(even_nums) > sum(odd_nums):
    result = even_nums.symmetric_difference(odd_nums)
    result = [str(el) for el in result]
    print(f"{', '.join(result)}")
