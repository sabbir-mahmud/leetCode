def nForest(n: int):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    # Example usage
    print("Right Angled Triangle Star Pattern of size 5:")
    nForest(5)
