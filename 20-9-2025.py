# Hàm print:
# sử dụng để in ra màn hình
print("Hello, World!")
# đặt biệt, có thể in nhiều giá trị cùng lúc
print("Hello", "World", "from", "Python")
# gọi biến
x = 42
y = "The answer is"
# in ra biến
print(y, x)
# Hàm input:
# sử dụng để nhận dữ liệu từ bàn phím
name = input("Enter your name: ")
print("Hello, " + name + "!")
# hàm type trả về kiểu dữ liệu của biến
print("Type of x:", type(x))
print("Type of y:", type(y))


# chương trình mẫu tương tác với người dùng
age = input("Enter your age: ")
age = int(age)  # chuyển đổi chuỗi nhập vào thành số nguyên
next_year_age = age + 1
print("Next year, you will be", next_year_age, "years old.")

