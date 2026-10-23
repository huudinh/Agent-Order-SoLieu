# PROMPT — B4·B5·B6 RA ORDER

> Tri thức: `so-A` §4–§6 · `so-D` · `so-C`.

---

## 1 · Chạy cổng A

```
Chạy cổng A cho yêu cầu này. In đủ 8 ô ĐẠT/TRƯỢT,
ô nào trượt phải nói rõ thiếu gì và cần ai cấp.

⛔ Chưa qua đủ 8 ô thì chưa in phiếu cho người yêu cầu duyệt.
```

Bằng công cụ:
```bash
python tools/order.py kiem out/ORD-2026-1023-MKT-01.json
```

---

## 2 · Dựng mẫu báo cáo cho cổng B

```
Dựng MẪU báo cáo cho phiếu này.

Yêu cầu:
- Số trong mẫu phải NHÌN LÀ BIẾT GIẢ — dùng 1.000 · 2.000 hoặc [số mẫu].
- Đủ cột, đủ dòng tổng, đủ dòng so sánh kỳ trước.
- Có đủ BA DÒNG bắt buộc ở đầu bảng:
    loại doanh số · mốc thời gian · phạm vi + nguồn + giờ cập nhật
- Kèm ba câu hỏi cho người duyệt:
    thiếu cột nào không · ba dòng định nghĩa đúng chưa ·
    nhìn bảng này có ra được quyết định như lúc đầu nói không
```

⚠️ ⛔ **Không dùng số trông như thật.** Sẽ có người chụp màn hình mẫu đi báo cáo, và đó là tai nạn khó gỡ.

---

## 3 · Bàn giao kỹ thuật

```
Xuất gói bàn giao cho kỹ thuật, đủ ba phần:
① Phiếu Order 14 trường
② Mẫu báo cáo đã duyệt
③ Tiêu chí nghiệm thu ĐẾM ĐƯỢC

Kèm cảnh báo nếu có: mốc lệch mặc định · rủi ro dữ liệu · giả định agent tự đặt.
```

Bằng công cụ *(chỉ chạy được khi qua cả hai cổng)*:
```bash
python tools/order.py bangiao out/ORD-2026-1023-MKT-01.json -o out/bangiao.md
```

---

## Nghiệm thu — viết thế nào cho đếm được

| ⛔ Không nhận | ✅ Nhận |
|---|---|
| *"Báo cáo dễ nhìn"* | *"Mặt bảng có đủ ba dòng định nghĩa"* |
| *"Chạy mượt"* | *"Mở dưới 5 giây với dữ liệu 12 tháng"* |
| *"Số phải đúng"* | *"Tổng tháng 9 khớp sổ Kế toán, lệch dưới 1%"* |
| *"Đầy đủ thông tin"* | *"Lọc một chiến dịch bất kỳ ra đúng số ca trong CRM"* |

**Phép thử:** đọc tiêu chí lên, hai người có thể **bất đồng** về việc nó đạt hay chưa không? Có → viết lại.

---

## Khi bị ép bỏ cổng

```
Em làm được ngay ạ. Nhưng có [n] chỗ chưa rõ — nếu đoán sai thì dựng xong
phải làm lại từ đầu, mất nhiều hơn là trả lời bây giờ.
Em hỏi gọn [n] câu trong 2 phút rồi chạy luôn.
```

Vẫn bị ép → dùng mặc định, **in đậm khối GIẢ ĐỊNH**, vẫn bắt duyệt ở cổng B.
⛔ **Riêng bảy câu định nghĩa thì không bỏ được** — đó là thứ quyết định con số.
