from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

print("\n CHUONG TRINH QUAN LY SINH VIEN ")
print("*********************MENU*********************")
print("\n1.Them sinh vien ")
print("\n2.Cap nhat thong tin sinh vien ")
print("\n3.Xoa sinh vien ")
print("\n4.Tim sinh vien theo ten ")
print("\n5.Sap xep sinh vien theo diem TB ")
print("\n6.Sap xep sinh vien theo ten chuyen nganh ")
print("\n7.Danh sach sinh vien ")
print("\n0.Exit ")
while (1==1):
    key= int(input("Nhap lua chon: " ))
    if(key == 1 ):
        print("\n1.Them sinh vien ")
        qlsv.nhapSV()
        print("\nThêm sinh viên thành công !")
    elif(key == 2 ):
        if (qlsv.soLuongSV() > 0):
            print("\n2.Cap nhat thong tin sinh vien ")
            print("\nNhap ID:")
            ID = int(input())
            qlsv.updateSV(ID) 
        else:
            print("\nDanh sach sinh vien trong!")
    elif(key == 3 ):
        if(qlsv.soLuongSV()> 0 ):
            print("\n3.Xoa sinh vien ")
            print("\n Nhap ID:")
            ID = int(input())
            if(qlsv.deleteById(ID)):
                print("\nSinh vien co ID = ",ID, "da bi xoa ")
            else:
                print("\nSinh vien co ID = ",ID, "khong ton tai ") 
        else:
            print("Danh sach trong !")
    elif(key == 4 ):
        if(qlsv.soLuongSV()>0 ):
            print("\n4.Tim kiem theo ten ")
            print("\n Nhap ten: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSV(searchResult) 
        else:
            print("\nDanh sach trong !")
    elif(key == 5):
        if(qlsv.soLuongSV() > 0):
            print("\n5.Sap xep sinh vien theo diem TB")
            qlsv.sortByDiemTb()
            qlsv.showSV(qlsv.getListSV())
        else:
            print("\nDanh sach trong!")
    elif(key == 6 ):
        if(qlsv.soLuongSV() > 0):
            print("\n Sap xep sinh vien theo ten ")
            qlsv.sortByName()
            qlsv.showSV(qlsv.getListSV())
        else:
            print("\nDanh sach trong !")
    elif(key == 7 ):
        if(qlsv.soLuongSV() > 0):
            print("\n7.Danh sach sinh vien")
            qlsv.showSV(qlsv.getListSV())
        else:
            print("\nDanh sach trong!")
    elif(key == 0):
        print("\nBan muon thoat?!")
        break
    else:
        print("\nKhong co chuc nang!")
        print("\nHay chon chuc nang trong MENU")