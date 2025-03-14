def tinhtongchan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0 :
            tong += num
    return tong

inputlist = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numB = list(map(int, inputlist.split(',')))

tongchan = tinhtongchan(numB)
print("Tong cac so chan: ", tongchan)