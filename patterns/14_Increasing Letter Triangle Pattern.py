def increasing_letter_triangle(n):
    ch = ord("A")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(ch), end=" ")
            ch += 1
        ch = ord("A")
        print()


if __name__ == "__main__":
    increasing_letter_triangle(5)
