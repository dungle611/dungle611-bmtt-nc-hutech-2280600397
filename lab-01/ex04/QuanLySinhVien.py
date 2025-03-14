from SinhVien import SinhVien

class QuanLySinhVien:
    listSV = []

    def generateID(self):
        maxId = 1
        if (self.soLuongSV()>0):
            maxId = self.listSV[0]._id
            for sv in self.listSV:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSV(self):
        return self.listSV.__len__()
    
    def nhapSV(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem TB cua sinh vien: "))
        sv = SinhVien( svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSV.append(sv)

    def updateSV(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem TB cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai. ", format(ID))

    def sortByID(self):
        self.listSV.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSV.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTb(self):
        self.listSV.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSV()>0):
            for sv in self.listSV:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSv = []
        if (self.soLuongSV() > 0):
            for sv in self.listSV:
                if (keyword.upper() in sv._name.upper()):
                    listSv.append(sv)
        return listSv

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSV.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if ( sv._diemTB >= 8):
            sv._hocluc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocluc = "Kha"
        elif (sv._diemTB >=5):
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"
    
    def showSV(self, listSv):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format("ID", "Name", "Sex", "Major", "DiemTB", "Hoc Luc"))
        if (listSv.__len__()>0):
            for sv in listSv:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print("\n")

    def getListSV(self):
        return self.listSV