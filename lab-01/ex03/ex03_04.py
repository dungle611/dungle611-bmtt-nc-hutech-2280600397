def truyCapPhanTu(tuple_data):
    firstElemental = tuple_data[0]
    lastElemental = tuple_data[-1]
    return firstElemental, lastElemental

inputTuple = eval(input("Nhap tuple, vi du (1,2,3):"))
first, last = truyCapPhanTu(inputTuple)

print("Phan tu dau tien: ", first)
print("Phan tu cuoi cung: ", last)