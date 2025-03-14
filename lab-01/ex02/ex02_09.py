def kiemtrasonguyen(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True
numB = int(input("Nhap vao so can kiem tra: "))
if kiemtrasonguyen(numB):
    print(numB, "la so nguyen to")
else:
    print(numB, "khong phai la so nguyen to.")