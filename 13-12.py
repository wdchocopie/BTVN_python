# 1. Khởi tạo một danh sách (List) chứa 3 phần tử chuỗi ban đầu
Tên = ["Stupid", "Skibidi toilet", "Poop"]

# 2. Sử dụng phương thức .append() để thêm phần tử "Kha" vào vị trí cuối cùng của danh sách
Tên.append("Kha")

# 3. Truy cập phần tử ở vị trí đầu tiên (index 0) và thay thế nó bằng một chuỗi rỗng
# (Lúc này chữ "Stupid" sẽ bị mất và thay bằng "")
Tên[0] = ""

# 4. Sử dụng vòng lặp for để duyệt qua từng phần tử trong danh sách "Tên"
# Biến 'i' sẽ lần lượt đại diện cho từng giá trị trong danh sách ở mỗi lần lặp
for i in Tên:
    # 5. In giá trị của biến 'i' ra màn hình console
    print(i)
