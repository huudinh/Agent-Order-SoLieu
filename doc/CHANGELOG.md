# CHANGELOG

## v1.0 — 2026-10-23
Bản đầu. Dựng theo mô tả viết tay của Team Số liệu HCI: *tiếp nhận Order từ các phòng ban, đặc biệt Marketing, các thương hiệu và tập đoàn → phân tích yêu cầu → người dùng duyệt → chuyển kỹ thuật*.

**Có gì**
- Bộ não `SYSTEM-PROMPT.md` (16 §) + `SYSTEM-PROMPT-NGAN.md` (**6.896** ký tự, vừa trần 8.000 của ChatGPT).
- 6 module tri thức · 4 prompt mẫu · schema phiếu Order 14 trường · mẫu 4 báo cáo.
- `tools/order.py` — chạy cổng A bằng máy, in phiếu, sinh gói bàn giao.

**Bốn thứ thêm so với mô tả gốc**

| Thêm | Vì sao |
|---|---|
| **Bảy câu định nghĩa doanh số** | Mô tả gốc ghi *"hiểu được định nghĩa Data / Marketing"*. Bảy câu là bản làm được của ý đó — và nó là cổng chặn, không phải lời khuyên |
| **Cổng A 8 ô chạy được bằng máy** | Mô tả gốc có bước *"Verify"*. Đặt mã cho từng ô để biết trượt ở đâu, và để script kiểm được |
| **Luật cộng ngang** | Bốn báo cáo trong mô tả gốc dùng bốn trục khác nhau. Không nói rõ thì sẽ có người cộng chúng lại |
| **Ba loại yêu cầu** (định kỳ · một lần · khẩn) | Loại *"một lần"* bị nhầm thành *"định kỳ"* là cách một đội ngập trong dashboard không ai mở |

**Quyết định thiết kế đáng nói**
- Agent **không có dữ liệu và không được đoán số**. Đây là ranh giới cứng, không phải hạn chế tạm thời — một agent vừa nhận yêu cầu vừa trả lời số sẽ bị hỏi số nhiều hơn là được nhờ viết Order.
- Phiếu mẫu `template/phieu-order.mau.json` **cố ý để trượt ô A4**, để người cài thấy cổng chặn hoạt động ngay lần chạy đầu.

**Chưa có — việc của giai đoạn sau**
- ⚠️ **Bảy câu định nghĩa dùng chung toàn tập đoàn chưa được Kế toán ký.** Chừng nào chưa ký, agent vẫn phải hỏi lại từng ca. Đây là việc có đòn bẩy cao nhất.
- Bảng nguồn dữ liệu trong `so-E` còn `[CHỜ XÁC NHẬN]` toàn bộ — tên hệ thống, tên bảng, người sở hữu, độ trễ.
- Chưa có danh mục báo cáo đang chạy → ô **A8** chưa rà trùng được.
- Chưa có khoá định danh khách dùng chung toàn tập đoàn → báo cáo ④ **chỉ dựng được ở mức doanh số, chưa dựng được ở mức khách**.
- Chưa có công cụ xuất phiếu Order ra Excel để lưu danh mục.
