def taoTupleTuList(lst):
    return tuple(lst)

inputList = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numB = list(map(int, inputList.split(',')))

myTuple = taoTupleTuList(numB)
print("List: ",numB)
print("Tuple tu list: ",myTuple)