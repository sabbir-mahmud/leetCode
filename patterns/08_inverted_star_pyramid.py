def nStarTriangle(n: int) -> None:
    """
    Print a star triangle of height n.
    """
    for i in range(n, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")

        # Print stars
        for j in range(2 * i - 1):
            print("*", end=" ")

        print()


if __name__ == "__main__":
    # Example usage
    print("Star Triangle Pattern of size 5:")
    nStarTriangle(5)
