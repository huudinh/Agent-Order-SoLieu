# NGUỒN DỮ LIỆU & GIỚI HẠN
Version 1.0 · Cập nhật 2026-10-23

> ⚠️ Toàn bộ file này là **khung để điền**. Tên hệ thống, tên bảng, người sở hữu phải do Team Số liệu xác nhận. Agent **không được đoán** tên bảng hay tên cột.

---

## 1 · Bảng nguồn — `[CHỜ XÁC NHẬN]` toàn bộ

| Nguồn | Cấp dữ liệu gì | Độ mịn | Độ trễ | Người sở hữu |
|---|---|---|---|---|
| **CRM** (Caresoft) | Lead · hội thoại · booking · đến khám | Theo khách | `[CHỜ XÁC NHẬN]` | `[CHỜ XÁC NHẬN]` |
| **ERP / phần mềm viện** | Ca thực hiện · doanh số · thu tiền | Theo ca | `[CHỜ XÁC NHẬN]` | `[CHỜ XÁC NHẬN]` |
| **Meta Ads** | Chi · hiển thị · click · inbox | Theo chiến dịch/ngày | ~vài giờ | Ads |
| **Google Ads** | Chi · click · chuyển đổi | Theo chiến dịch/ngày | ~vài giờ | Ads |
| **Google Analytics** | Phiên · hành vi trên site | Theo phiên | ~24h | Ads |
| **Kế toán** | Thu thực tế · hoàn huỷ | Theo chứng từ | Theo kỳ khoá sổ | Kế toán |

⚠️ **Hai nguồn hay bị nhầm là một:** số của **nền tảng quảng cáo** và số của **CRM**. Meta đếm *messaging conversation started*; CRM đếm liên hệ đã kiểm. Chênh **15–30%** là bình thường — ⛔ không phải lỗi, nhưng **phải ghi rõ báo cáo đang dùng nguồn nào**.

---

## 2 · Bốn câu phải hỏi về nguồn, cho mọi Order

```
[ ] Dữ liệu này nằm ở hệ thống nào, bảng nào?
[ ] Ai là người sở hữu và chịu trách nhiệm về chất lượng số đó?
[ ] Độ trễ bao lâu — số hôm nay xem được lúc nào?
[ ] Lịch sử có bao xa — so cùng kỳ năm trước có dữ liệu không?
```

⚠️ **Câu 4 hay bị bỏ qua và nó chặn cả báo cáo.** Xin *"so với cùng kỳ năm trước"* mà hệ thống mới chạy 8 tháng thì cột đó vĩnh viễn trống. Phát hiện ở cổng A rẻ hơn phát hiện lúc nghiệm thu.

---

## 3 · Độ mịn — xin mịn hơn mức dữ liệu có là xin điều không thể

| Muốn cắt theo | Cần dữ liệu ở mức |
|---|---|
| Tháng | Theo ngày |
| Cơ sở | Mỗi ca có gắn cơ sở |
| Chiến dịch quảng cáo | Mỗi lead có gắn **nguồn** từ lúc sinh ra |
| Nhân viên | Mỗi ca có gắn người phụ trách |
| Khách đa thương hiệu | **Khoá định danh khách dùng chung toàn tập đoàn** |

⛔ **Gắn nguồn cho lead phải làm từ ngày đầu.** Không có trường nguồn lúc tạo lead thì ba tháng sau **không cắt ngược lại được** — và báo cáo ① Doanh số MKT không dựng được. Đây là việc 30 phút ở tuần đầu, hoặc là việc không bao giờ làm được nữa.

---

## 4 · Ba rủi ro dữ liệu phải ghi vào Order

| Rủi ro | Dấu hiệu | Ghi gì vào Order |
|---|---|---|
| **Nhập liệu không đều** | Cùng một dịch vụ có nhiều cách gõ tên | Cần bảng chuẩn hoá tên dịch vụ, ai duy trì |
| **Khoá sổ muộn** | Số tháng trước còn đổi sau ngày 10 | Ghi rõ *"số tháng N chốt sau ngày X"* |
| **Khách trùng** | Một người nhiều hồ sơ | Ghi quy tắc khử trùng, hoặc chấp nhận và nêu rõ |

---

## 5 · Quyền riêng tư — ranh giới cứng

⛔ **Báo cáo chạy trên số tổng hợp, không chạy trên danh sách khách.**

| ⛔ Không đưa vào báo cáo | ✅ Thay bằng |
|---|---|
| Tên · SĐT · email · địa chỉ khách | Mã khách, hoặc chỉ số đếm |
| Dịch vụ gắn với một người cụ thể | Phân bố theo nhóm |
| Ảnh · hồ sơ bệnh án | Không đưa vào, không trích dẫn |

⚠️ **Dịch vụ thẩm mỹ gắn với một người là thông tin sức khoẻ**, không phải thông tin marketing thông thường. Báo cáo cần ví dụ minh hoạ thì dùng `KH-001`, `KH-002`.

Người yêu cầu cần danh sách khách để gọi điện → đó là **yêu cầu vận hành CRM**, ⛔ không phải yêu cầu báo cáo. Chuyển đúng kênh.
