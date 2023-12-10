# Đọc X và Y từ input
with open('CHIAQUA.INP', 'r') as file:
    X, Y = map(int, file.readline().split())

# Tìm tất cả các phương án chia quà thoả mãn điều kiện
solutions = []
for n in range(1, max(X, Y) + 1):
    if X % n == 0 and Y % n == 0:
        a = X // n
        b = Y // n
        solutions.append((n, a, b))

# Ghi các phương án vào file output
with open('CHIAQUA.OUT', 'w') as file:
    file.write(str(len(solutions)) + '\n')
    for solution in solutions:
        file.write(' '.join(map(str, solution)) + '\n')
