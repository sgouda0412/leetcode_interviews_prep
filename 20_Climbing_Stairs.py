
def climbStairs(n: int) -> int:
    f = 1
    s = 1
    for i in range(n - 1):
        t = f
        f = f + s
        s = t

    return f


if __name__ == "__main__":
    n = 3
    print(climbStairs(n))