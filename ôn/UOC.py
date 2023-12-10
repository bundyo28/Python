# Đọc số nguyên dương n từ input
with open('UOC.INP', 'r') as file:
    n = int(file.readline())

# Tìm các ước của n
factors = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        factors.append(i)
        if i != n // i:
            factors.append(n // i)

# Sắp xếp các ước theo thứ tự tăng dần
factors.sort()

# Ghi các ước vào file output
with open('UOC.OUT', 'w') as file:
    for factor in factors:
        file.write(str(factor) + '\n')
