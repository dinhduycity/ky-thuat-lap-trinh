print("le dinh duy")
print("235752021610087")
import math

def Tinh(R):
    if R <= 0:
        return "Bán kính không hợp lệ! Vui lòng nhập số dương."
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    
    return f"Chu vi hình tròn: {chu_vi:.2f}\nDiện tích hình tròn: {dien_tich:.2f}"

try:
    R = float(input("Nhập bán kính hình tròn: "))
    print(Tinh(R))
except ValueError:
    print("Vui lòng nhập một số hợp lệ!")
