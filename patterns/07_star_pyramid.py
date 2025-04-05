def nStarTriangle(n):
    # Loop through each row
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end=" ")

        # Print stars
        for j in range(2 * i + 1):
            print("*", end=" ")
        # Move to the next line after each row
        print()


if __name__ == "__main__":
    # Example usage
    print("Star Pyramid Pattern of size 5:")
    nStarTriangle(5)
