print("le dinh duy")
print("235752021610087")

s = input("nhap chuoi: ").split()
element_to_find = input("tim kiem: ")
try:
    index = s.index(element_to_find)
    print(f"{element_to_find} vi tri: {index}")
except ValueError:
    print(f"{element_to_find}ko co trong danh sach.")
