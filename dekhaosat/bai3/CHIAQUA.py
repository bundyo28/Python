# doc X , Y tu file inp
with open('CHIAQUA.INP', 'r') as file:
    X, Y = map(int, file.readline().split())

#Tim tat ca cac phuong an chia qua thoa man dieu kien
solutions = []
for n in range(1, max(X, Y) + 1):
    if X % n == 0 and Y % n == 0:
        a = X // n
        b = Y // n
        solutions.append((n, a, b))

# ghi cac phuong an vao file out
with open('CHIAQUA.OUT', 'w') as file:
    file.write(str(len(solutions)) + '\n')
    for solution in solutions:
        file.write(' '.join(map(str, solution)) + '\n')
