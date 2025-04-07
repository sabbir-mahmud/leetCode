def alpha_hill(n):
    ch = ord("A")
    for i in range(n):
        print("  " * (n - i), end="")
        for j in range(i + 1):
            print(chr(ch), end=" ")
            ch += 1

        ch -= 1
        for j in range(i, 0, -1):
            ch -= 1
            print(chr(ch), end=" ")
        ch = ord("A")
        print()


if __name__ == "__main__":
    alpha_hill(6)
