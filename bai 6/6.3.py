print("le dinh duy")
print("235752021610087")

class Nguoi:
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

aNam = Nam()
aNu = Nu()

print(aNam.getGender())  
print(aNu.getGender())   
