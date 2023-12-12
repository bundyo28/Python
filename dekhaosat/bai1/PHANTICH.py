def phantichso(n):
    kqua = []
    start = 1
    end = 2
    tong_hien_tai = start + end

    while start < n:
        if tong_hien_tai == n:
            sequence = list(range(start, end + 1))
            kqua.append(sequence)
            tong_hien_tai -= start
            start += 1
        elif tong_hien_tai < n:
            end += 1
            tong_hien_tai += end
        else:
            tong_hien_tai -= start
            start += 1

    return kqua

# doc so nguyen tu file inp
with open('PHANTICH.INP', 'r') as file:
    n = int(file.read())

#phan tich so thanh tong cac so tu nhien lien tiep
kqua = phantichso(n)

# ghi ket qua vao file out
with open('PHANTICH.OUT', 'w') as file:
    if len(kqua) == 0:
        file.write('0')
    else:
        for sequence in kqua:
            file.write('+'.join(map(str, sequence)) + '\n')
