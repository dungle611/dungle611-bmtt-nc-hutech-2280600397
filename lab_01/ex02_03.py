#Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))
#Kiểm tra xem số đó có phải số chẵn hay không
print("số chẵn" if so % 2 == 0 else "số lẻ")
