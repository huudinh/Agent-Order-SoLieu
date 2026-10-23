# PHIẾU ORDER — 14 TRƯỜNG
Version 1.0 · Cập nhật 2026-10-23

> Đây là **vật bàn giao** giữa người yêu cầu và kỹ thuật. Thiếu trường nào thì kỹ thuật sẽ hỏi lại, và mỗi lần hỏi lại là mất một vòng.
> Schema máy đọc được: [`template/phieu-order.schema.json`](../template/phieu-order.schema.json).

---

## Mười bốn trường

| # | Trường | Bắt buộc | Ghi chú |
|---|---|:-:|---|
| 1 | `ma_order` | ✅ | `ORD-<yyyy-mmdd>-<bộ phận>-<số>` |
| 2 | `nguoi_yeu_cau` | ✅ | Tên + bộ phận + thương hiệu |
| 3 | `nguoi_duyet` | ✅ | Người ký ở cổng B. Có thể trùng trường 2 |
| 4 | `cau_hoi_kinh_doanh` | ✅ | Một câu. ⛔ Không phải mô tả bảng |
| 5 | `quyet_dinh_di_kem` | ✅ | Số ra xấu thì làm gì, ra đẹp thì làm gì |
| 6 | `loai_bao_cao` | ✅ | Một trong 6 loại ở `so-C`, hoặc `khac` |
| 7 | `dinh_nghia` | ✅ | **Bảy câu** của `so-B` — thiếu một câu là cổng A trượt |
| 8 | `chi_so` | ✅ | Từng chỉ số: tên · công thức · **tử số** · **mẫu số** · đơn vị |
| 9 | `chieu_cat` | ✅ | Cắt theo gì: thời gian · cơ sở · dịch vụ · nguồn · nhân viên |
| 10 | `pham_vi_thoi_gian` | ✅ | Kỳ báo cáo + kỳ so sánh |
| 11 | `nguon_du_lieu` | ✅ | Hệ thống nào · bảng nào · ai sở hữu |
| 12 | `tan_suat` | ✅ | Một lần / ngày / tuần / tháng + giờ cập nhật |
| 13 | `nghiem_thu` | ✅ | Tiêu chí **đếm được** — xem `so-A` §6 |
| 14 | `han_chot` | ✅ | Ngày cần có + mức ưu tiên |

**Trường tuỳ chọn nhưng nên có:** `bao_cao_lien_quan` (tránh trùng) · `rui_ro_du_lieu` · `gia_dinh` (những gì agent tự mặc định).

---

## Khuôn in ra cho người duyệt

Bản này là bản **người đọc**, không phải bản kỹ thuật. In ở cổng B.

```
PHIẾU ORDER  ORD-2026-1023-MKT-01
─────────────────────────────────────────────────────────
NGƯỜI YÊU CẦU : Chị A — Phòng Marketing, Kangnam
NGƯỜI DUYỆT   : Chị A
CÂU HỎI       : Tiền quảng cáo line Mũi tháng 10 có về không?
QUYẾT ĐỊNH    : Xấu → cắt ngân sách nhóm kém. Đẹp → tăng 20% cho nhóm tốt.
LOẠI BÁO CÁO  : ① Doanh số MKT

ĐỊNH NGHĨA ĐÃ CHỐT
  Loại doanh số  : ghi nhận (đã ký phiếu, chưa cần thu đủ tiền)
  Mốc thời gian  : ngày chốt
  Gồm / trừ      : TRỪ hoàn huỷ · giá sau chiết khấu · thẻ trả trước tính khi DÙNG
  Tính ai        : khách mới + khách cũ quay lại do chiến dịch
  Quy về         : nguồn lead → chiến dịch
  VAT            : trước VAT
  Đa dịch vụ     : tách theo dịch vụ, combo phân bổ theo giá niêm yết

CHỈ SỐ
  CPL            = chi ÷ lead hợp lệ
  Tỷ lệ chốt     = ca chốt ÷ ĐẾN KHÁM        ← chú ý mẫu số
  ROAS           = doanh số ÷ chi
  Độ trễ         = số ngày trung bình lead → chốt

CHIỀU CẮT     : tháng · chiến dịch · dịch vụ
KỲ            : 01–31/10/2026, so với 01–30/09/2026
NGUỒN         : Meta Ads · Google Ads · CRM Caresoft   [CHỜ XÁC NHẬN tên bảng]
TẦN SUẤT      : hằng tuần, 8:00 thứ Hai
HẠN           : 30/10/2026 · ưu tiên cao

NGHIỆM THU
  [ ] Tổng doanh số khớp CRM, lệch dưới 1%
  [ ] Lọc chiến dịch bất kỳ ra đúng số ca trong CRM
  [ ] Có đủ ba dòng ghi chú bắt buộc trên mặt bảng

GIẢ ĐỊNH AGENT TỰ ĐẶT   ← phải có nếu người yêu cầu nói "em không rành"
  - Mốc ngày chốt là mặc định của loại báo cáo ①
─────────────────────────────────────────────────────────
```

---

## Ba lỗi viết Order hay gặp

| Lỗi | Ví dụ | Sửa |
|---|---|---|
| **Mô tả bảng thay vì câu hỏi** | *"Em cần bảng có cột tháng, cột doanh số, cột %"* | Hỏi ngược: *"để quyết định việc gì?"* rồi mới dựng cột |
| **Chỉ số không có mẫu số** | *"Tỷ lệ chốt"* | Ghi rõ `÷ đến khám`, không phải `÷ lead` |
| **Nghiệm thu không đếm được** | *"Báo cáo dễ nhìn"* | Đổi thành một phép so khớp có con số |

---

## Vòng đời một Order

```
NHÁP → ĐÃ DUYỆT (cổng B) → ĐANG DỰNG → NGHIỆM THU → ĐANG CHẠY
                                              ↓ không đạt
                                           SỬA LẠI
```

- Đổi yêu cầu **sau khi đã duyệt** → ⛔ không sửa Order cũ. Mở **phiên bản mới** `-v2`, ghi rõ đổi gì và vì sao. Sửa đè là cách mất dấu lý do.
- Order **ĐANG CHẠY** mà 3 tháng không ai mở → đưa vào danh sách rà soát. Dashboard không ai dùng vẫn tốn công bảo trì.
