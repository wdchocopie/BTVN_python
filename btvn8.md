
# 🏰 NHIỆM VỤ LẬP TRÌNH: CUỘC PHIÊU LƯU CỦA HIỆP SĨ TÍ

👋 **Chào mừng các Lập trình viên nhí!**
Hôm nay, các em sẽ đóng vai **Người kiến tạo thế giới**. Nhiệm vụ của em là viết mã lệnh (Python) để điều khiển Hiệp sĩ Tí đi phiêu lưu.

---

## 🛠️ PHẦN 1: CHUẨN BỊ HÀNH TRANG

Trước khi bắt đầu, Hiệp sĩ Tí cần có tiền và sức khỏe. Em hãy tạo ra 3 "cái hộp" (biến số) để lưu giữ thông tin này nhé.

**👉 Yêu cầu:**
1. Tạo biến `vang` và cho Tí **100** đồng.
2. Tạo biến `mau` (sức khỏe) và cho Tí **50** điểm.
3. Tạo biến `balo` là một danh sách, bên trong có sẵn món đồ `"Bánh mì"`.

```python
# Gợi ý:
vang = ___
mau = ___
balo = ["___"]

```

---

## ⚔️ PHẦN 2: ĐI MUA VŨ KHÍ (HÀM & PHÉP TOÁN)

Tí gặp một bác thợ rèn. Bác bán một thanh **Kiếm Gỗ** giá **20 đồng**.
Em hãy viết một hành động (Hàm) tên là `mua_vu_khi` để Tí trả tiền.

**👉 Yêu cầu:**

1. Định nghĩa hàm `def mua_vu_khi():`
2. Sử dụng lệnh `global vang` để xin phép dùng túi tiền.
3. Lấy số tiền hiện tại trừ đi 20.
4. In ra màn hình dòng chữ: *"Đã mua kiếm gỗ!"*

**🧩 Cấu trúc gợi ý:**

```python
def mua_vu_khi():
    global vang
    # Con hãy viết phép trừ ở dòng dưới nhé (vang bằng vang trừ 20)
    vang = ___ - 20
    print("Đã mua kiếm gỗ!")
    print("Số vàng còn lại:", vang)

```

---

## 🎒 PHẦN 3: NHẶT ĐỒ (DANH SÁCH)

Trên đường đi, Tí thấy một **"Bình máu"** rơi trên cỏ. Em hãy viết hàm `nhat_do` để nhặt nó bỏ vào balo.

**👉 Yêu cầu:**

1. Định nghĩa hàm `def nhat_do():`
2. Dùng lệnh `.append(...)` để thêm `"Bình máu"` vào danh sách `balo`.
3. In ra danh sách các món đồ đang có trong balo.

**🧩 Cấu trúc gợi ý:**

```python
def nhat_do():
    # Dùng lệnh append để thêm đồ vào balo
    balo.append("___")
    print("Đã nhặt được đồ mới!")
    print("Balo hiện có:", balo)

```

---

## 🐉 PHẦN 4: CHIẾN ĐẤU (NẾU... THÌ...)

😱 Ối! Một con Rồng Lửa xuất hiện chặn đường. Tí phải quyết định dựa trên sức khỏe của mình.

**👉 Yêu cầu:** Viết hàm `gap_quai_vat` sử dụng câu lệnh `if` (nếu) và `else` (nếu không):

* **Nếu** `mau` nhỏ hơn 30: In ra *"Nguy hiểm quá! Chạy thôi!"*
* **Nếu không** (nghĩa là máu còn nhiều): In ra *"Xông lên! Tí chiến đấu!"*

**🧩 Cấu trúc gợi ý:**

```python
def gap_quai_vat():
    print("--- GẶP QUÁI VẬT ---")
    
    # Con hãy điền điều kiện vào chỗ trống (mau < 30)
    if ___ < ___:
        print("Nguy hiểm quá! Chạy thôi!")
    else:
        print("Xông lên! Tí chiến đấu!")

```

---

## 🚀 PHẦN 5: CHẠY TRÒ CHƠI

Tuyệt vời! Em đã dạy cho Tí tất cả các kỹ năng cần thiết. Bây giờ hãy ra lệnh cho Tí thực hiện chúng theo thứ tự câu chuyện nhé.

**👉 Yêu cầu:**
Gọi tên các hàm em vừa viết ở trên theo thứ tự:

1. Mua vũ khí.
2. Nhặt đồ.
3. Gặp quái vật.

```python
print("=== TRÒ CHƠI BẮT ĐẦU ===")

# Gọi hàm mua vũ khí
mua_vu_khi()

# Gọi hàm nhặt đồ
___()

# Gọi hàm gặp quái vật
___()

```

