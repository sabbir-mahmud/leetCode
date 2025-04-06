def number_crown(n):
    for i in range(1, n + 1):
        # Left side numbers
        left = [str(j) for j in range(1, i + 1)]

        # Right side numbers
        right = [str(j) for j in range(i, 0, -1)]

        # Spaces between the crowns
        space = "  " * (n - i) * 2

        # Build the full row and print once
        print(" ".join(left) + space + " ".join(right))


if __name__ == "__main__":
    number_crown(5)
