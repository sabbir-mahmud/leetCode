def nTriangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


if __name__ == "__main__":
    # Example usage
    print("Right Angled Number Pyramid Pattern of size 5:")
    nTriangle(5)
