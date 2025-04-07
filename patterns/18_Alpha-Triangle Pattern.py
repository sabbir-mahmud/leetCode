def alpha_triangle(n):
    ch = ord("A") + n - 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(ch), end=" ")
            ch -= 1
        ch = ord("A") + n - 1
        print()


if __name__ == "__main__":
    alpha_triangle(5)
