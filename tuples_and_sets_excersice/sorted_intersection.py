num_of_ranges = int(input())

longest_intersection = set()

for i in range(num_of_ranges):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")
    first_set = {i for i in range(int(first_start), int(first_end)+1)}
    second_set = {i for i in range(int(second_start), int(second_end)+1)}

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
longest_intersection = [str(el) for el in longest_intersection]
print(f"Longest intersection is [{', '.join(longest_intersection)}] with length {len(longest_intersection)}")