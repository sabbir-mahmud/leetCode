def climbStairs(n: int) -> int:
    if n <= 1 or n >= 45:
        return

    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


if __name__ == "__main__":
    climbStairs(4)
