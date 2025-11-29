# **Đề bài:** Viết chương trình trò chơi "Vượt qua 3 cửa ải".

**Quy định:**
*   Khai báo một danh sách (List) chứa đúng 3 mật khẩu theo thứ tự: \["111", "222", "333"\].
*   Người chơi phải nhập đúng mật khẩu cửa thứ nhất (index 0), rồi mới được nhập cửa thứ hai (index 1), cuối cùng là cửa thứ ba (index 2).
**Hoạt động:**
*   Sử dụng một biến đếm (ví dụ i = 0) để xác định đang đứng ở cửa nào.   
*   Sử dụng vòng lặp while chạy khi người chơi chưa qua hết 3 cửa (tức là khi i < 3).    
*   Trong vòng lặp:    
    *   Yêu cầu nhập mật khẩu cho cửa hiện tại.        
    *   Nếu nhập **Đúng** (khớp với mật khẩu trong danh sách tại vị trí i): In ra "Qua ải!" và tăng i lên 1 (để chuyển sang cửa tiếp theo).        
    *   Nếu nhập **Sai**: In ra "Sai rồi, nhập lại!" (giữ nguyên i để bắt nhập lại cửa đó).        
*   Khi vòng lặp kết thúc: In ra "CHIẾN THẮNG!".
