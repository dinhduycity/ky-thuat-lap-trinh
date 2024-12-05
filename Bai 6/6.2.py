print("le dinh duy")
print("235752021610087")

# Định nghĩa class Hinhchunhat
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

# Tạo đối tượng hình chữ nhật với chiều dài 8 và chiều rộng 4
hcn = Hinhchunhat(8, 4)

# Gọi method dien_tich để tính diện tích
dien_tich_hcn = hcn.dien_tich()
print("Diện tích hình chữ nhật là:", dien_tich_hcn)

