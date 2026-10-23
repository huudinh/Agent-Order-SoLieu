# BỐN BÁO CÁO DOANH SỐ + HAI BÁO CÁO PHÁI SINH
Version 1.0 · Cập nhật 2026-10-23

> Bốn báo cáo lõi theo yêu cầu gốc của Team Số liệu, cộng hai báo cáo phái sinh hay được xin kèm.
> **Mỗi báo cáo có trục riêng và mốc thời gian riêng** — xem luật cộng ngang ở [`so-B-tu-dien-doanh-so.md`](so-B-tu-dien-doanh-so.md) §2.

---

## Bảng tra nhanh

| Báo cáo | Ai xin | Trả lời câu hỏi gì | Trục | Mốc mặc định đề xuất |
|---|---|---|---|---|
| ① **Doanh số MKT** | Marketing | *Tiền quảng cáo đổ ra có về không?* | Nguồn lead | Ngày chốt |
| ② **Doanh số Cơ sở** | Giám đốc cơ sở | *Cơ sở này chạy ra bao nhiêu?* | Nơi thực hiện | Ngày thực hiện |
| ③ **Doanh số Thương hiệu** | Ban thương hiệu | *Brand này đang đi lên hay xuống?* | Thương hiệu | Ngày thu tiền |
| ④ **Doanh số Tập đoàn** | Ban điều hành | *Cả tập đoàn hôm nay đứng ở đâu?* | Toàn tập đoàn | Ngày thu tiền |
| ⑤ **Doanh số dịch vụ** | Ban dịch vụ | *Line nào đáng đổ nguồn lực?* | Dịch vụ / line | Theo báo cáo mẹ |
| ⑥ **Kết cấu doanh số MKT** | Marketing | *Doanh số đến từ đâu, theo tỷ lệ nào?* | Nguồn × dịch vụ | Theo ① |

---

## ① Doanh số MKT

**Câu hỏi kinh doanh:** tiền quảng cáo đổ ra có về không, và về từ kênh nào.

| Hạng mục | Nội dung |
|---|---|
| **Trục** | Nguồn lead → chiến dịch → nhóm quảng cáo → nội dung |
| **Mốc đề xuất** | **Ngày chốt** — khớp với công của Sales và với kỳ chạy quảng cáo |
| **Phạm vi khách** | Khách **mới** + khách cũ **quay lại do chiến dịch**. ⛔ Không tính walk-in |
| **Cột lõi** | Chi quảng cáo · Lead · CPL · Đến khám · Ca chốt · Doanh số · **ROAS** · Chi phí/ca chốt |
| **Phải có trên mặt bảng** | Mốc thời gian · loại doanh số · *"không cộng ngang với báo cáo Cơ sở"* |

⚠️ **Bẫy thứ hai — quy gán nguồn.** Báo cáo cắt theo **kênh** (SEO-Web · Ads · Fanpage · Zalo) bắt buộc chốt thêm **câu thứ tám** ở `so-B` §1b: khách đi qua nhiều kênh thì kênh nào được tính công. Không chốt thì mỗi team tự hiểu một kiểu, và tổng các team lớn hơn doanh số thật.

⚠️ **Bẫy đặc trưng:** khách thấy quảng cáo tháng 9, đến khám tháng 10, chốt tháng 11. Báo cáo theo **ngày chốt** sẽ gán doanh số tháng 11 cho chi phí tháng 9 → ROAS tháng 11 đẹp giả, tháng 9 xấu giả.
→ **Bắt buộc có cột `độ trễ lead → chốt`**, hoặc đọc theo **cohort** chứ không đọc theo tháng lịch. Ghi rõ điều này trong Order.

---

## ② Doanh số Cơ sở

**Câu hỏi kinh doanh:** cơ sở này tạo ra bao nhiêu, công suất dùng tới đâu.

| Hạng mục | Nội dung |
|---|---|
| **Trục** | Cơ sở → phòng/ghế → bác sĩ/kỹ thuật viên |
| **Mốc đề xuất** | **Ngày thực hiện** — vì đây là báo cáo công suất, không phải báo cáo tiền |
| **Phạm vi khách** | **Tất cả** khách đến cơ sở, gồm cả walk-in và khách chuyển từ cơ sở khác |
| **Cột lõi** | Lượt đến · Ca thực hiện · Doanh số · Doanh số/ngày công · Công suất · Tỷ lệ huỷ |
| **Phải có** | Dòng ghi chú về **khách chuyển cơ sở** — khách chốt ở A làm ở B thì tính cho ai |

⚠️ **Bẫy đặc trưng:** khách chốt tại cơ sở Hà Nội nhưng làm tại TP.HCM. Nếu hai cơ sở cùng tính thì tổng cơ sở **lớn hơn** tổng tập đoàn. Phải chốt một quy tắc và in nó lên bảng.

---

## ③ Doanh số Thương hiệu

**Câu hỏi kinh doanh:** brand này đang đi lên hay đi xuống, so với kỳ trước và so với brand khác.

| Hạng mục | Nội dung |
|---|---|
| **Trục** | Thương hiệu → cơ sở → dịch vụ |
| **Mốc đề xuất** | **Ngày thu tiền** — để khớp sổ Kế toán |
| **Phạm vi** | Gộp từ báo cáo ② **nếu cùng mốc**; khác mốc thì phải dựng riêng |
| **Cột lõi** | Doanh số · % so kỳ trước · % so cùng kỳ năm trước · Doanh số/khách · Số khách mới |
| **Phải có** | So sánh **cùng loại kỳ** — tháng 30 ngày không so thẳng với tháng 28 ngày |

⚠️ **Bẫy đặc trưng:** so tháng này với tháng trước mà không chỉnh theo số ngày làm việc, số ngày lễ, mùa vụ. Kết luận *"giảm 12%"* có khi chỉ là *"tháng này ít hơn 2 ngày làm việc"*.

---

## ④ Doanh số Tập đoàn

**Câu hỏi kinh doanh:** cả tập đoàn đang ở đâu so với kế hoạch.

| Hạng mục | Nội dung |
|---|---|
| **Trục** | Tập đoàn → thương hiệu → ngành hàng |
| **Mốc đề xuất** | **Ngày thu tiền** |
| **Phạm vi** | Toàn bộ, **đã khử trùng** khách dùng nhiều thương hiệu |
| **Cột lõi** | Doanh số · % kế hoạch · Đóng góp từng brand · Doanh số/khách · Số khách duy nhất |
| **Phải có** | Quy tắc **khử trùng khách đa thương hiệu** và quy tắc **loại giao dịch nội bộ** |

⚠️ **Bẫy đặc trưng:** một khách dùng dịch vụ ở hai thương hiệu trong tập đoàn. Nếu đếm *"số khách"* bằng cách cộng hai brand thì khách đó bị đếm hai lần, và chỉ số *doanh số/khách* bị sai theo.
→ Bắt buộc có **khoá định danh khách dùng chung toàn tập đoàn**. `[CHỜ XÁC NHẬN]` hệ thống đã có khoá này chưa — nếu chưa thì **báo cáo ④ chỉ dựng được ở mức doanh số, chưa dựng được ở mức khách**.

---

## ⑤ Doanh số dịch vụ *(phái sinh)*

Cắt bất kỳ báo cáo nào ở trên theo **dịch vụ / line**. Không phải báo cáo độc lập — nó là một chiều cắt.

⚠️ **Bẫy đặc trưng:** gói combo nhiều dịch vụ. Phải có **quy tắc phân bổ** (theo giá niêm yết từng phần? theo tỷ lệ cố định? gán hết vào dịch vụ chính?). Không có quy tắc thì mỗi lần dựng ra một số khác.

---

## ⑥ Kết cấu doanh số Marketing *(phái sinh)*

Phân rã báo cáo ① theo **tỷ trọng**: nguồn nào đóng góp bao nhiêu phần trăm, dịch vụ nào trong nguồn đó.

**Dùng để trả lời:** *"nên dồn tiền vào đâu"* — không phải *"tháng này được bao nhiêu"*.

⚠️ Báo cáo tỷ trọng **không đọc được khi mẫu nhỏ**. Dưới `[CHỜ XÁC NHẬN: ngưỡng tối thiểu]` ca thì tỷ lệ phần trăm nhảy loạn giữa các tháng và dễ dẫn tới quyết định sai. Ghi ngưỡng này lên mặt bảng.

---

## Ba dòng bắt buộc in trên MỌI báo cáo

```
Loại doanh số : [ghi nhận / thực thu / đã thực hiện]
Mốc thời gian : [ngày chốt / ngày thực hiện / ngày thu tiền]
Phạm vi       : [khách nào · cơ sở nào · gồm/trừ gì]  ·  Nguồn: [hệ thống]  ·  Cập nhật: [lúc nào]
```

⛔ **Thiếu ba dòng này thì báo cáo không được phát hành.** Không phải vì hình thức — mà vì nếu không có, hai bảng khác định nghĩa sẽ bị đem ra so với nhau, và cuộc họp sẽ nói về số thay vì nói về việc.
