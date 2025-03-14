def daonguoc(lst):
    return lst[::-1]

inputlist = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numB = list(map(int, inputlist.split(',')))

listDaoNguoc = daonguoc(numB)
print("List sau khi dao nguoc: ", listDaoNguoc)