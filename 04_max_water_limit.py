def maxArea(height):
    ans = 0
    l = 0
    r = len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        ans = max(ans, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return ans


if __name__ == "__main__":
    h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(h))
