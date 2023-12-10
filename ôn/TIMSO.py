def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Đọc P và Q từ file input
with open('TIMSO.INP', 'r') as file:
    P, Q = map(int, file.readline().split())

# Tìm các số X thỏa mãn yêu cầu
result = []
for X in range(P + 1, Q):
    Y = int(str(X)[::-1])  # Số đảo ngược của X

    if is_prime(Y):
        result.append(X)

# Ghi kết quả vào file output
with open('TIMSO.OUT', 'w') as file:
    for X in result:
        file.write(str(X) + '\n')
