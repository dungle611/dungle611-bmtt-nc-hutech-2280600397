def xoaPhanTu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
myDict = {'a': 1, 'b' : 2, 'c': 3, 'd': 4 }
keyToDelete = 'b'
result = xoaPhanTu(myDict, keyToDelete)
if result:
    print("Phan tu da duoc xoa tu dictionary: ", myDict)
else:
    print("khong tim thay phan tu can xoa trong Dictionary.")