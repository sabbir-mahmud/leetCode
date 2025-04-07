def symmetric_void_pattern(n):
    for i in range(n, 0, -1):
        star = "*" * i
        space = "  " * (n - i) if n - i != 0 else ""
        print(f"{star}{space}{star}")

    for i in range(1, n + 1):
        star = "*" * i
        space = "  " * (n - i) if n - i != 0 else ""
        print(f"{star}{space}{star}")


if __name__ == "__main__":
    symmetric_void_pattern(5)
