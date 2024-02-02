from typing import List

def rob(nums: List[int]) -> int:
    r1 = r2 = 0

    for n in nums:
        t = max(r1 + n, r2)
        r1 = r2
        r2 = t

    return r2




if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(rob(nums))
