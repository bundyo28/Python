# Đọc số nguyên dương n từ input
with open('UOC.INP', 'r') as file:
    n = int(file.readline())

# Tìm các ước của n
so = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        so.append(i)
        if i != n // i:
            so.append(n // i)

# Sắp xếp các ước theo thứ tự tăng dần
so.sort()

# Ghi các ước vào file output
with open('UOC.OUT', 'w') as file:
    for factor in so:
        file.write(str(factor) + '\n')
