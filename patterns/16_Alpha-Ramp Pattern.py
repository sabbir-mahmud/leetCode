def alpha_ramp_pattern(n):
    ch = ord("A")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(ch), end=" ")

        ch += 1

        print()


if __name__ == "__main__":
    alpha_ramp_pattern(5)
