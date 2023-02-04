def math_operations(*numbers, **nums_to_operate):
    for i in range(len(numbers)):
        key = list(nums_to_operate.keys())[i % 4]

        if key == "a":
            nums_to_operate[key] += numbers[i]
        elif key == "s":
            nums_to_operate[key] -= numbers[i]
        elif key == "d":
            if numbers[i] != 0:
                nums_to_operate[key] /= numbers[i]
        elif key == "m":
            nums_to_operate[key] *= numbers[i]

    nums_to_operate = sorted(nums_to_operate.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{k}: {v:.1f}" for k, v in nums_to_operate)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))