# 02 — CÂU LỆNH

## Theo từng bước

| Bước | Gõ |
|---|---|
| **B1–B2 tiếp nhận** | `Có yêu cầu báo cáo mới. Tiếp nhận giúp tôi. NGƯỜI YÊU CẦU: … HỌ NÓI: "…"` |
| **B3 chốt định nghĩa** | `Chốt bảy câu định nghĩa cho báo cáo [loại].` |
| **B4 cổng A** | `Chạy cổng A. In đủ 8 ô ĐẠT/TRƯỢT, ô nào trượt nói rõ thiếu gì và ai cấp.` |
| **B5 cổng B** | `Dựng mẫu báo cáo cho phiếu này. Số phải nhìn là biết giả.` |
| **B6 bàn giao** | `Xuất gói bàn giao kỹ thuật, đủ ba phần.` |
| **Nghiệm thu** | `Kỹ thuật dựng xong rồi. Chạy nghiệm thu theo tiêu chí trong phiếu.` |

Prompt đầy đủ cho từng bước nằm trong [`prompts/`](../prompts/).

---

## Câu hỏi vận hành hỏi thẳng được

```
Marketing và Kế toán đang ra hai số khác nhau cho cùng tháng 9. Rà giúp tôi.
```
```
Yêu cầu này có trùng với báo cáo nào đang chạy không?
```
```
Dữ liệu hiện tại có đủ để cắt theo chiến dịch không?
```
```
Báo cáo này nên là dashboard định kỳ hay chỉ một truy vấn một lần?
```
```
Rà danh mục báo cáo quý này: cái nào nên giữ, gộp, hay ngừng?
```

---

## Lệnh nửa tay

```bash
python tools/order.py kiem    <phieu.json>              # cổng A, 8 ô
python tools/order.py phieu   <phieu.json> [-o ra.md]   # in phiếu bản người đọc
python tools/order.py bangiao <phieu.json> [-o ra.md]   # gói bàn giao kỹ thuật
python tools/gop-tham-khao.py                           # gộp tri thức
```

### Hai thứ script tự chặn
1. **Cổng A chưa đủ 8 ô** → ⛔ không bàn giao.
2. **Người duyệt chưa ký** (`nguoi_duyet.ngay_duyet` trống) → ⛔ không bàn giao.

### Bốn thứ script cảnh báo mà không chặn
- Mốc thời gian **lệch mặc định** của loại báo cáo đó
- Tiêu chí nghiệm thu **không đếm được** (*dễ nhìn · chạy mượt · đầy đủ*)
- Tần suất *"một lần"* mà chưa ghi **KHÔNG BẢO TRÌ**
- Phiếu có **GIẢ ĐỊNH** do agent tự đặt mà chưa chắc người duyệt đã đọc

---

## Khi agent trả lời sai

| Dấu hiệu | Gõ |
|---|---|
| Nhận đơn ngay, chưa hỏi mục tiêu | `Chưa hỏi "để quyết định việc gì". Quay lại B1.` |
| Đưa ra một con số | `Bạn không có dữ liệu. Chuyển người sở hữu số liệu, đừng đoán.` |
| Bỏ qua bảy câu | `Chưa chốt đủ bảy câu định nghĩa. Cổng A ô A2 trượt.` |
| Chỉ số thiếu mẫu số | `Tỷ lệ này chia cho cái gì? Ghi rõ mẫu số.` |
| Đoán tên bảng | `Đừng đoán tên bảng. Ghi [CHỜ XÁC NHẬN] và nêu ai cấp.` |
| Nghiệm thu mơ hồ | `"Dễ nhìn" không nghiệm thu được. Đổi thành phép so khớp có con số.` |
| Nhận "xem nhanh" rồi dựng dashboard | `Đây là yêu cầu một lần. Không dựng dashboard, ghi rõ không bảo trì.` |

---

## Ba câu khách hay hỏi mà agent phải từ chối

| Họ hỏi | Agent trả lời |
|---|---|
| *"Cho chị xem nhanh doanh số tháng 9"* | *"Em không giữ số ạ. Số đó anh/chị lấy từ [người sở hữu]. Còn nếu cần xem hằng tháng thì em làm phiếu order luôn."* |
| *"Cho chị danh sách khách để gọi"* | *"Báo cáo chạy trên số tổng hợp ạ. Danh sách khách là việc của CRM, em chuyển sang [bộ phận]."* |
| *"Gấp lắm, bỏ qua mấy câu hỏi đi"* | *"Em hỏi gọn [n] câu trong 2 phút rồi chạy luôn — đoán sai thì dựng xong phải làm lại từ đầu."* |
