def nTriangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(i + 1, end=" ")
        print()


if __name__ == "__main__":
    # Example usage
    print("Right Angled Number Pyramid Pattern of size 5:")
    nTriangle(5)
