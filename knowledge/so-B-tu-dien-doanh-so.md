# TỪ ĐIỂN DOANH SỐ — BẢY CÂU PHẢI CHỐT TRƯỚC KHI RA ORDER
Version 1.0 · Cập nhật 2026-10-23 · **file quan trọng nhất của gói này**

> ⚠️ Bảng định nghĩa dưới đây là **bản đề xuất để chốt**, không phải chính sách đang có hiệu lực. Mỗi dòng phải được **Team Số liệu + Kế toán** ký xác nhận một lần, rồi dùng chung cho mọi báo cáo. Chừng nào chưa ký, agent vẫn phải hỏi lại từng ca.

---

## 0 · Vì sao file này đứng đầu

> **"Doanh số" không phải một con số. Nó là một câu hỏi chưa hỏi xong.**

Tình huống có thật và lặp đi lặp lại: Marketing xin *"doanh số tháng 10 của line Mũi"*. Kỹ thuật dựng xong. Marketing xem rồi nói *"sao thấp thế, bên em ghi nhận cao hơn nhiều"*. Kế toán xem rồi nói *"số này cao hơn sổ của chị"*. **Cả ba đều đúng** — vì ba người đang nói về ba con số khác nhau mà ai cũng gọi là *doanh số*.

Mỗi lần như vậy mất **ít nhất một vòng dựng lại**, và lần sau không ai tin bảng nữa.

→ Vì vậy agent **không chuyển Order sang kỹ thuật** khi chưa chốt đủ **bảy câu** dưới đây.

---

## 1 · Bảy câu chốt định nghĩa

Mỗi phiếu Order phải trả lời đủ bảy câu. Thiếu câu nào → cổng A trượt.

### Câu 1 — Doanh số **ghi nhận** hay **thực thu**?

| Loại | Nghĩa | Ai hay dùng |
|---|---|---|
| **Ghi nhận** (booked) | Khách đã chốt dịch vụ, đã ký phiếu — dù chưa thu đủ tiền | Marketing · Sales |
| **Thực thu** (collected) | Tiền đã vào tài khoản hoặc đã nhận tại quầy | Kế toán · Tài chính |
| **Đã thực hiện** (delivered) | Dịch vụ đã làm xong cho khách | Vận hành · Cơ sở |

⚠️ Ba con số này **luôn khác nhau** ở ngành có trả góp, đặt cọc và liệu trình nhiều buổi.
⛔ Không có mặc định. Hỏi.

### Câu 2 — Tính theo **ngày nào**?

| Mốc | Nghĩa | Hệ quả |
|---|---|---|
| **Ngày chốt** | Ngày khách đồng ý và ký | Khớp với công của Sales và Marketing |
| **Ngày thực hiện** | Ngày làm dịch vụ | Khớp với công suất cơ sở |
| **Ngày thu tiền** | Ngày tiền vào | Khớp với sổ Kế toán |

> **Một ca đặt cọc tháng 9, làm tháng 10, trả nốt tháng 11 sẽ rơi vào ba tháng khác nhau tuỳ mốc chọn.** Đây là nguyên nhân số một của chênh lệch giữa báo cáo Marketing và sổ Kế toán.

### Câu 3 — **Gộp hay trừ** những khoản này?

```
[ ] Hoàn tiền / huỷ ca        → trừ vào tháng phát sinh hay tháng gốc?
[ ] Chiết khấu, khuyến mãi    → tính theo giá niêm yết hay giá thực?
[ ] Voucher, thẻ trả trước    → ghi nhận khi bán thẻ hay khi dùng thẻ?
[ ] Trả góp                   → ghi nhận trọn gói hay theo kỳ?
[ ] Dịch vụ tặng kèm          → tính 0đ hay tính theo giá niêm yết?
```

⚠️ **Thẻ trả trước là bẫy lớn nhất.** Ghi nhận lúc bán thẻ thì tháng đó đẹp, tháng sau trống; ghi nhận lúc dùng thẻ thì ngược lại. Phải chốt một lần cho mọi báo cáo.

### Câu 4 — Tính **ai**?

```
[ ] Khách mới (lần đầu đến thương hiệu)
[ ] Khách cũ quay lại
[ ] Khách tái khám / làm tiếp liệu trình đã mua
[ ] Khách do nhân viên giới thiệu
[ ] Khách walk-in không qua marketing
```

Báo cáo **Doanh số MKT** thường chỉ tính nhóm 1 và 2; báo cáo **Cơ sở** tính hết. Không nói rõ thì hai bảng lệch nhau và không ai biết vì sao.

### Câu 5 — Quy về **đơn vị nào**?

| Trục | Dùng cho báo cáo |
|---|---|
| **Nguồn lead** (chiến dịch · kênh · nội dung) | Doanh số MKT |
| **Nhân viên** (sales · tư vấn · bác sĩ) | Báo cáo nhân sự |
| **Cơ sở** (nơi thực hiện) | Doanh số Cơ sở |
| **Thương hiệu** | Doanh số Thương hiệu |
| **Dịch vụ / line** | Doanh số dịch vụ |

⚠️ **Một ca có thể thuộc nhiều trục cùng lúc.** Khách do quảng cáo Hà Nội kéo về nhưng bay vào TP.HCM làm → tính doanh số MKT cho chiến dịch Hà Nội, tính doanh số Cơ sở cho TP.HCM. **Cùng một ca, hai báo cáo, không trùng lặp** — nhưng cộng hai bảng lại thì nhân đôi.

### Câu 6 — Đã gồm **VAT** chưa?
`[ ] Trước VAT` · `[ ] Sau VAT` — và ghi rõ mức.

### Câu 7 — Khách dùng **nhiều dịch vụ / nhiều thương hiệu** thì tính vào đâu?

```
[ ] Tách theo từng dịch vụ (phải có quy tắc phân bổ cho gói combo)
[ ] Gán hết vào dịch vụ chính
[ ] Tính ở cả hai, và CHẤP NHẬN không cộng ngang được
```

⚠️ Chọn phương án 3 thì **phải ghi cảnh báo lên mặt báo cáo**, nếu không sẽ có người cộng các dòng lại.

---

## 1b · ⚠️ CÂU THỨ TÁM — chỉ áp cho báo cáo ① MKT và ⑥ Kết cấu

> **Quy gán nguồn: khách đi qua nhiều kênh thì KÊNH NÀO được tính công?**

Bảy câu ở trên chốt *doanh số là gì*. Câu này chốt *ai được tính*. Với báo cáo của một team kênh — **SEO-Web · Ads · Fanpage · Zalo** — đây là câu **khó nhất và dễ cãi nhau nhất**, vì nó quyết định con số của chính team đó.

### Tình huống kinh điển

```
Khách tìm Google → đọc bài SEO → 3 ngày sau thấy quảng cáo Facebook
→ nhắn Fanpage → để lại số → chốt
```

| Quy tắc | Ai được tính | Hệ quả |
|---|---|---|
| **Chạm đầu** *(first touch)* | **SEO-Web** | Team SEO đẹp, team Ads kêu |
| **Chạm cuối** *(last touch)* | **Fanpage / Ads** | ⚠️ Mặc định của phần lớn CRM — và là lý do SEO luôn trông kém |
| **Chia đều** | Mỗi kênh một nửa | Tổng vẫn đúng, nhưng không kênh nào "sở hữu" ca đó |
| **Tính cho tất cả** | Cả hai cùng tính đủ | ⛔ **Tổng các kênh > tổng thật** — phải in cảnh báo |

### Ba luật bắt buộc

**① Chốt một quy tắc, dùng cho mọi báo cáo kênh.** Mỗi team một quy tắc khác nhau là cách tổng bốn team lớn hơn doanh số thật.

**② Nếu chọn "tính cho tất cả" thì ⛔ KHÔNG được cộng các bảng kênh lại.** Phải in lên mặt bảng: *"Một ca có thể xuất hiện ở nhiều kênh. ⛔ Không cộng ngang."*

**③ Báo cáo của một team kênh phải nêu rõ phần ca ĐƯỢC HỖ TRỢ.**
Ví dụ cho SEO-Web: *"120 ca tính cho SEO theo chạm đầu · trong đó 45 ca có chạm quảng cáo ở giữa"*. Con số thứ hai giữ cho cuộc họp khỏi biến thành tranh công.

### ⚠️ Điều kiện kỹ thuật — kiểm ở cổng A ô A4

Quy gán *chạm đầu* hoặc *chia đều* **chỉ làm được khi hệ thống lưu được lịch sử chạm của một khách**. Nếu CRM chỉ lưu **một trường nguồn duy nhất** ghi đè lần cuối thì:
- ⛔ Chỉ chạy được quy tắc **chạm cuối**.
- Agent phải nói thẳng điều này, ⛔ không hứa làm chạm đầu rồi để kỹ thuật phát hiện sau.

`[CHỜ XÁC NHẬN]` CRM có lưu lịch sử chạm không — đây là câu hỏi quyết định cả nhóm báo cáo kênh.

---

## 2 · ⚠️ Luật cộng ngang — điều hay bị vi phạm nhất

> **Doanh số MKT + Doanh số Cơ sở + Doanh số Thương hiệu ≠ Doanh số Tập đoàn.**

Bốn báo cáo dùng **bốn trục khác nhau** và **ba mốc thời gian khác nhau**. Chúng không phải bốn mảnh của một cái bánh — chúng là **bốn cách chụp cùng một cái bánh từ bốn góc**.

| Báo cáo | Trục | Mốc mặc định đề xuất | Không cộng được với |
|---|---|---|---|
| **Doanh số MKT** | Nguồn lead | Ngày chốt | Cơ sở, Tập đoàn |
| **Doanh số Cơ sở** | Nơi thực hiện | Ngày thực hiện | MKT |
| **Doanh số Thương hiệu** | Thương hiệu | Ngày thu tiền | — *(gộp được từ Cơ sở nếu cùng mốc)* |
| **Doanh số Tập đoàn** | Toàn tập đoàn | Ngày thu tiền | — *(phải khử trùng khách đa thương hiệu)* |

⛔ **Mọi báo cáo phải in trên mặt bảng:** mốc thời gian đang dùng · loại doanh số · phạm vi tính. Thiếu ba dòng này thì bảng đó sẽ bị đem đi so với bảng khác, và cuộc họp sẽ nói về định nghĩa thay vì nói về kinh doanh.

---

## 3 · Từ điển chỉ số marketing — chỗ thứ hai hay cãi nhau

| Chỉ số | Định nghĩa đề xuất | Chỗ hay lệch |
|---|---|---|
| **Lead** | Liên hệ có SĐT dùng được + có dịch vụ quan tâm, **đã qua lọc rác** | Lead-nền-tảng (Meta/Google) ≠ lead-CRM. Chênh **15–30%** là bình thường |
| **Lead rác** | Danh sách lý do **đóng được**, không để "cảm thấy rác" | Mỗi người lọc một kiểu |
| **Booking** | Lịch hẹn có **ngày–giờ–cơ sở** cụ thể và khách **đã xác nhận** | "Khách nói để sắp xếp rồi báo lại" ⛔ không phải booking |
| **Đến khám** | Đã có mặt tại cơ sở, ghi nhận trong CRM | Có nơi tính cả khách gọi xác nhận |
| **Ca chốt** | Khách đồng ý và đã ký phiếu dịch vụ | Trùng với câu 1 ở trên |
| **CPL** | Chi ÷ lead **hợp lệ** | Dùng lead thô thì CPL đẹp giả |
| **Tỷ lệ chốt** | Ca chốt ÷ **đến khám**, không phải ÷ lead | Chia nhầm mẫu số là lệch nhiều lần |

⚠️ **Mẫu số là chỗ sai nhiều hơn tử số.** Mỗi tỷ lệ trong Order phải ghi rõ **chia cho cái gì**.

---

## 4 · Cách agent dùng file này

1. Người yêu cầu nói *"doanh số"* → agent **không nhận đơn ngay**, hỏi bảy câu — **cộng câu thứ tám** nếu là báo cáo ① MKT hoặc ⑥ Kết cấu.
2. Người yêu cầu không biết trả lời → agent **đưa phương án mặc định đề xuất** của loại báo cáo đó (§2) và nói rõ *"đây là mặc định, chị xác nhận hoặc đổi"*.
3. Người yêu cầu nói *"em không rành, chị quyết hộ"* → agent chọn mặc định, **in đậm dòng GIẢ ĐỊNH** trong phiếu, và vẫn bắt duyệt ở cổng B.
4. Hai phiếu Order khác nhau dùng **hai định nghĩa khác nhau cho cùng một chữ** → agent **phải cảnh báo**, không im lặng làm cả hai.

⛔ **Agent không được tự chốt định nghĩa thay Kế toán.** Nó đề xuất và ghi rõ đó là đề xuất.
