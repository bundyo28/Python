def songuyento(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#doc P va Q tu file inp
with open('TIMSO.INP', 'r') as file:
    P, Q = map(int, file.readline().split())

# Tim cac so X tm yeu cau
ketqua = []
for X in range(P + 1, Q):
    Y = int(str(X)[::-1])  #So dao nguoc cua X

    if songuyento(Y):
        ketqua.append(X)

# ghi ket qua vao file out
with open('TIMSO.OUT', 'w') as file:
    for X in ketqua:
        file.write(str(X) + '\n' + '\n')
