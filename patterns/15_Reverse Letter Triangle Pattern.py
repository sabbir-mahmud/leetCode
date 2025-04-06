def reverse_latter_triangle(n):
    ch = ord("A")
    for i in range(n + 1, 0, -1):
        for j in range(1, i):
            print(chr(ch), end=" ")
            ch += 1
        ch = ord("A")
        print()


if __name__ == "__main__":
    reverse_latter_triangle(5)
