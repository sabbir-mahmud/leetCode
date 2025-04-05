def seeding(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    # Example usage
    print("Inverted Right Angled Number Pyramid Pattern of size 5:")
    seeding(5)
