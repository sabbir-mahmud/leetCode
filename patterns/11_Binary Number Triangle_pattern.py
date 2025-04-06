def nBinaryTriangle(n):
    for i in range(n):
        start = 1 if i % 2 == 0 else 0
        row = []
        for j in range(i + 1):
            row.append(str(start))
            start = 1 - start
        print(" ".join(row))


if __name__ == "__main__":
    nBinaryTriangle(5)
