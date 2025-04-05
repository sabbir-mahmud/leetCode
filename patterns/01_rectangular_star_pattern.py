def printSquare(n: int):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    # Example usage
    print("Square Star Pattern of size 5:")
    printSquare(5)
