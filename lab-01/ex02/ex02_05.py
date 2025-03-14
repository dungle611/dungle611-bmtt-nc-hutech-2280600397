sogiolam = float(input("Nhap so gio lam moi tuan: "))
luonggio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam,giotieuchuan)
thuclinh = giotieuchuan * luonggio +giovuotchuan * luonggio * 1.5
print(f"So tien thuc linh cua nhan vien: {thuclinh}")