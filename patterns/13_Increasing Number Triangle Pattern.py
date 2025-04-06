def nNumberTriangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i, i * 2):
            print(num, end=" ")
            num += 1
        print()


if __name__ == "__main__":
    nNumberTriangle(5)
