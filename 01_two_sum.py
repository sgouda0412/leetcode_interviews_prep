def two_sum(nums, target):
    lookup = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in lookup:
            return [lookup[target - value], index]
        
        lookup[value] = index
    return [-1, -1]


if __name__ == "__main__":
    nums = [2, 1, 9, 11]
    target = 9
    print(two_sum(nums, target))