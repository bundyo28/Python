def analyze_number(n):
    result = []
    start = 1
    end = 2
    current_sum = start + end

    while start < n:
        if current_sum == n:
            sequence = list(range(start, end + 1))
            result.append(sequence)
            current_sum -= start
            start += 1
        elif current_sum < n:
            end += 1
            current_sum += end
        else:
            current_sum -= start
            start += 1

    return result

# Đọc số nguyên từ file input
with open('PHANTICH.INP', 'r') as file:
    n = int(file.read())

# Phân tích số thành tổng các số tự nhiên liên tiếp
result = analyze_number(n)

# Ghi kết quả vào file output
with open('PHANTICH.OUT', 'w') as file:
    if len(result) == 0:
        file.write('0')
    else:
        for sequence in result:
            file.write('+'.join(map(str, sequence)) + '\n')
