def sisalgold(a, b, operasi):
    return operasi(a, b)

def kurang(x, y):
    return x - y

hasil = sisalgold(8, 2, kurang)
print(hasil)
