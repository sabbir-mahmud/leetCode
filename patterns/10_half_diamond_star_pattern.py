def half_diamond_star_pattern(n):
    # Print the upper half of the diamond
    for i in range(n + 1):
        print("*" * i)

    # Print the lower half of the diamond
    for i in range(n - 1):
        print("*" * (n - i - 1))


if __name__ == "__main__":
    # Example usage
    print("Half Diamond Star Pattern of size 5:")
    half_diamond_star_pattern(5)
