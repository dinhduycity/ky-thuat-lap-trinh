print("le dinh duy")
print("235752021610087")
def benefit(t, n, k):
    total_amount = n * (1 + t/100)**k
    return total_amount

t = float(input("Nhập lãi suất (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")
