def demSoLan(lst):
    countDict = {}
    for item in lst:
        if item in countDict:
            countDict[item] += 1
        else:
            countDict[item] = 1
    return countDict

inputString = input("Nhap danh sach cac tu, cach nhau bang dau cach: ")
wordList = inputString.split()

soLan = demSoLan(wordList)
print("So lan xuat hien cua cac phan tu: ", soLan)