def print_func(negative_num, positive_num):
    print(negative_num)
    print(positive_num)
    if abs(negative_num) > positive_num:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


def sum_of_negative_and_positive_nums(nums):
    sum_of_negative = 0
    sum_of_positive = 0

    for num in nums:
        if num > 0:
            sum_of_positive += num
        else:
            sum_of_negative += num

    return print_func(sum_of_negative, sum_of_positive)


numbers = [int(n) for n in input().split()]
sum_of_negative_and_positive_nums(numbers)