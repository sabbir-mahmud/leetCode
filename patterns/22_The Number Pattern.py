def number_patter(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            val = n - min(i, j, size - 1 - i, size - 1 - j)
            print(val, end=" ")
        print()


if __name__ == "__main__":
    number_patter(5)
