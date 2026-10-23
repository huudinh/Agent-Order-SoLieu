# MẪU BÁO CÁO — DÙNG Ở CỔNG B

> Đây là **mẫu để người yêu cầu nhìn trước khi kỹ thuật dựng**.
> ⚠️ Mọi số trong file này là **số giả**. Số thật không bao giờ tròn như vậy — đó là có chủ ý, để không ai chụp màn hình mẫu đi báo cáo.

---

## Ba dòng bắt buộc — in ở ĐẦU mọi báo cáo

```
┌────────────────────────────────────────────────────────────────┐
│ Loại doanh số : GHI NHẬN (đã ký phiếu, chưa cần thu đủ tiền)   │
│ Mốc thời gian : NGÀY CHỐT                                      │
│ Phạm vi       : khách mới + khách cũ quay lại do chiến dịch    │
│                 · trước VAT · đã trừ hoàn huỷ                  │
│ Nguồn: Meta Ads · Google Ads · CRM   Cập nhật: 08:00 23/10/2026│
└────────────────────────────────────────────────────────────────┘
```

⛔ Thiếu khối này thì báo cáo **không được phát hành** — không phải vì hình thức, mà vì nó sẽ bị đem so với bảng khác định nghĩa.

---

## ① Mẫu — Doanh số MKT

| Chiến dịch | Chi | Lead | CPL | Đến khám | Ca chốt | Tỷ lệ chốt | Doanh số | ROAS | Độ trễ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Mũi · Tìm kiếm | 10.000 | 100 | 100 | 40 | 10 | 25,0% | 50.000 | 5,0 | 12 ngày |
| Mũi · Meta | 20.000 | 300 | 67 | 60 | 12 | 20,0% | 60.000 | 3,0 | 21 ngày |
| Mũi · TikTok | 5.000 | 80 | 63 | 8 | 1 | 12,5% | 5.000 | 1,0 | 30 ngày |
| **Tổng** | **35.000** | **480** | **73** | **108** | **23** | **21,3%** | **115.000** | **3,3** | **18 ngày** |
| *So tháng trước* | *+9%* | *+15%* | *−5%* | *+4%* | *−8%* | *−12%* | *−3%* | *−11%* | *+4 ngày* |

**Ghi chú bắt buộc dưới bảng:**
- `Tỷ lệ chốt = ca chốt ÷ ĐẾN KHÁM` *(không phải ÷ lead)*
- `CPL = chi ÷ lead HỢP LỆ` *(đã lọc rác, không phải lead thô từ nền tảng)*
- ⚠️ Bảng này tính theo **ngày chốt** — ⛔ **không cộng ngang** với báo cáo Doanh số Cơ sở
- ⚠️ Độ trễ trung bình **18 ngày**: doanh số tháng này một phần đến từ chi phí tháng trước

---

## ② Mẫu — Doanh số Cơ sở

| Cơ sở | Lượt đến | Ca thực hiện | Doanh số | DS/ngày công | Công suất | Tỷ lệ huỷ |
|---|---:|---:|---:|---:|---:|---:|
| Hà Nội | 500 | 200 | 400.000 | 15.000 | 80% | 5% |
| TP.HCM | 400 | 160 | 350.000 | 14.000 | 75% | 7% |
| **Tổng** | **900** | **360** | **750.000** | **14.500** | **78%** | **6%** |

**Ghi chú bắt buộc:**
- Tính theo **ngày thực hiện** · gồm cả khách walk-in
- ⚠️ Khách chốt ở cơ sở A, làm ở cơ sở B → tính cho **cơ sở thực hiện**
- ⛔ Tổng bảng này **không bằng** tổng Doanh số MKT (khác trục, khác mốc)

---

## ③④ Mẫu — Thương hiệu & Tập đoàn

| Thương hiệu | Doanh số | % kế hoạch | So kỳ trước | So cùng kỳ năm trước | Khách duy nhất | DS/khách |
|---|---:|---:|---:|---:|---:|---:|
| Kangnam | 800.000 | 95% | +5% | +12% | 2.000 | 400 |
| Nha khoa Paris | 300.000 | 88% | −2% | +6% | 1.000 | 300 |
| **Tập đoàn** | **1.100.000** | **93%** | **+3%** | **+10%** | **2.800** | **393** |

**Ghi chú bắt buộc:**
- Tính theo **ngày thu tiền** · sau VAT
- ⚠️ **Khách duy nhất của tập đoàn (2.800) nhỏ hơn tổng hai brand (3.000)** — đã khử trùng 200 khách dùng cả hai thương hiệu
- ⚠️ So kỳ trước đã chuẩn hoá theo **số ngày làm việc**, không so thẳng tổng

---

## Ba câu hỏi gửi kèm khi trình mẫu

```
Chị xem giúp em ba điều:
1. Thiếu cột nào chị cần không?
2. Ba dòng định nghĩa ở đầu bảng đã đúng ý chị chưa?
3. Nhìn bảng này chị có ra được quyết định như lúc đầu mình nói không?
```

⚠️ **Câu 3 là câu quan trọng nhất.** Bảng đủ cột mà không ra được quyết định thì vẫn là bảng hỏng — và lúc đó phải quay lại B1, không phải thêm cột.
