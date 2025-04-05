def nStarDiamond(n: int) -> None:
    """Prints a diamond star pattern of size n."""
    # Upper half
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    # Lower half
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

    print()


if __name__ == "__main__":
    print(f"Diamond star pattern of size {5}:")
    nStarDiamond(5)
