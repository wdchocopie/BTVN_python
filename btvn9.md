# BTVN9

copy đoạn code này vào python online và tiếp tục làm
```
# --- PHẦN 1: ĐỊNH NGHĨA CÁC HÀM (LOGIC) ---
# Hãy code tiếp ở phần 1 để phần số 2 hoạt động
# Gợi ý hãy sử dụng return để trả về giá trị

# --- PHẦN 2: CHƯƠNG TRÌNH CHÍNH (GIAO DIỆN), Không cần thay đổi ---

def may_tinh():
    print("========= MÁY TÍNH ĐƠN GIẢN =========")
    print("Chọn phép tính:")
    print("1. Cộng (+)")
    print("2. Trừ (-)")
    print("3. Nhân (*)")
    print("4. Chia (/)")
    
    # Nhập lựa chọn
    lua_chon = input("Nhập lựa chọn của bạn (1/2/3/4): ")

    # Kiểm tra xem lựa chọn có hợp lệ không
    if lua_chon in ('1', '2', '3', '4'):
        try:
            # Ép kiểu float để tính được số thập phân
            so1 = float(input("Nhập số thứ nhất: "))
            so2 = float(input("Nhập số thứ hai: "))

            if lua_chon == '1':
                print(f"-> Kết quả: {so1} + {so2} = {cong(so1, so2)}")

            elif lua_chon == '2':
                print(f"-> Kết quả: {so1} - {so2} = {tru(so1, so2)}")

            elif lua_chon == '3':
                print(f"-> Kết quả: {so1} * {so2} = {nhan(so1, so2)}")

            elif lua_chon == '4':
                ket_qua = chia(so1, so2)
                if ket_qua == "Lỗi! Không thể chia cho 0":
                    print(ket_qua)
                else:
                    print(f"-> Kết quả: {so1} / {so2} = {ket_qua}")
        
        except ValueError:
            print("Lỗi: Vui lòng chỉ nhập số!")
    else:
        print("Lựa chọn không hợp lệ!")

# --- CHẠY CHƯƠNG TRÌNH, không cần thay đổi ---
# Gọi hàm may_tinh để bắt đầu
may_tinh()
```
