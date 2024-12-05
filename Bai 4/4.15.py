print("le dinh duy")
print("235752021610087")

s = input("Nhập các từ tiếng Anh, cách nhau bởi dấu cách: ")
words = s.split()
words.sort()
print("Các từ theo thứ tự từ điển:")
for word in words:
    print(word)
