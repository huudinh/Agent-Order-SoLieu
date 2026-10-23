# 📊 AGENT-ORDER-SOLIEU — Tiếp nhận yêu cầu báo cáo

> Version 1.0 · AI **tiếp nhận yêu cầu báo cáo** từ phòng Marketing · các thương hiệu · tập đoàn · cơ sở → hỏi cho rõ → **chốt định nghĩa** → ra **Phiếu Order** đủ để Team Số liệu dựng được ngay.

Kiến trúc **BRAIN brand-neutral** ([`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md)) + **MODULE nguồn dữ liệu tách riêng** ([`knowledge/so-E-nguon-du-lieu.md`](knowledge/so-E-nguon-du-lieu.md)) → đổi tập đoàn chỉ cần thay module.

**Phục vụ:** Team Số liệu — HCI Group.

---

## Nguyên tắc tối thượng

> ### "Doanh số" không phải một con số. Nó là một câu hỏi chưa hỏi xong.

Marketing xin *"doanh số tháng 10 line Mũi"*. Kỹ thuật dựng xong. Marketing xem rồi nói *"sao thấp thế"*. Kế toán xem rồi nói *"sao cao hơn sổ của chị"*.

**Cả ba đều đúng** — ba người đang nói về ba con số khác nhau mà ai cũng gọi là *doanh số*.

> **Giá trị của agent nằm ở chỗ nó HỎI, không nằm ở chỗ nó làm.**
> Dashboard dựng sai phải dựng lại từ đầu. Câu hỏi sai chỉ mất một lượt trả lời.

---

## Agent đứng ở đâu

```
Phòng Marketing ─┐
Các thương hiệu ─┤→  AGENT-ORDER-SOLIEU  →  Team Số liệu / kỹ thuật
Tập đoàn        ─┤    hỏi · chốt định nghĩa      dựng dashboard, báo cáo
Cơ sở           ─┘    · ra Phiếu Order
```

| Agent **làm** | Agent ⛔ **không làm** |
|---|---|
| Hỏi mục tiêu và quyết định đi kèm | Dựng dashboard |
| Chốt bảy câu định nghĩa | Truy vấn cơ sở dữ liệu |
| Dựng **mẫu báo cáo** để người yêu cầu nhìn trước | **Trả lời một con số bất kỳ** |
| Viết **Phiếu Order 14 trường** | Chốt định nghĩa thay Kế toán |
| Viết **tiêu chí nghiệm thu đếm được** | Duyệt thay người yêu cầu |

---

## Quy trình 6 bước — hai cổng chặn

```
B1 MUỐN GÌ      → B2 NHẬP THÔNG TIN → B3 CHỐT ĐỊNH NGHĨA ★
                                              ↓
B6 RA ORDER  ←  ⛔ B5 CỔNG B DUYỆT  ←  ⛔ B4 CỔNG A VERIFY
```

| Cổng | Khi nào | Trượt thì sao |
|---|---|---|
| **A — Verify** · 8 ô | Trước khi trình người yêu cầu | **A2** (bảy câu định nghĩa) trượt → quay lại B3. Ô trượt nhiều nhất |
| **B — Duyệt** | Trước khi chuyển kỹ thuật | Chưa xác nhận → ⛔ không bàn giao |

---

## ★ Bảy câu định nghĩa — cổng chặn thật của gói này

```
1. Doanh số GHI NHẬN (đã ký) / THỰC THU (tiền về) / ĐÃ THỰC HIỆN (làm xong)?
2. Tính theo NGÀY nào: ngày chốt / ngày thực hiện / ngày thu tiền?
3. GỒM hay TRỪ: hoàn huỷ · chiết khấu · voucher & thẻ trả trước · trả góp · dịch vụ tặng?
4. Tính AI: khách mới / khách cũ / tái khám / walk-in?
5. Quy về ĐƠN VỊ nào: nguồn lead / nhân viên / cơ sở / thương hiệu / dịch vụ?
6. Trước hay sau VAT?
7. Khách dùng NHIỀU dịch vụ hoặc NHIỀU thương hiệu thì tính vào đâu?
```

⚠️ **Câu 2 là câu đắt nhất.** Một ca đặt cọc tháng 9, làm tháng 10, trả nốt tháng 11 sẽ rơi vào **ba tháng khác nhau** tuỳ mốc chọn. Đây là nguyên nhân số một của chênh lệch giữa báo cáo Marketing và sổ Kế toán.

---

## ⚠️ Luật cộng ngang

> **Doanh số MKT + Cơ sở + Thương hiệu ≠ Doanh số Tập đoàn.**

Bốn báo cáo dùng **bốn trục** và **ba mốc thời gian** khác nhau. Chúng không phải bốn mảnh của một cái bánh — chúng là **bốn cách chụp cùng một cái bánh từ bốn góc**.

| Báo cáo | Trục | Mốc mặc định | Bẫy đặc trưng |
|---|---|---|---|
| ① **Doanh số MKT** | Nguồn lead | Ngày chốt | Độ trễ lead→chốt làm ROAS theo tháng lịch bị lệch |
| ② **Doanh số Cơ sở** | Nơi thực hiện | Ngày thực hiện | Khách chốt ở A làm ở B — tính cho ai |
| ③ **Doanh số Thương hiệu** | Thương hiệu | Ngày thu tiền | So kỳ không chuẩn hoá theo số ngày làm việc |
| ④ **Doanh số Tập đoàn** | Toàn tập đoàn | Ngày thu tiền | Khách dùng nhiều brand bị đếm hai lần |
| ⑤ Doanh số dịch vụ *(phái sinh)* | Dịch vụ | theo báo cáo mẹ | Gói combo chưa có quy tắc phân bổ |
| ⑥ Kết cấu doanh số MKT *(phái sinh)* | Nguồn × dịch vụ | theo ① | Tỷ trọng không đọc được khi mẫu nhỏ |

**Ba dòng bắt buộc in trên MỌI báo cáo:** loại doanh số · mốc thời gian · phạm vi + nguồn + giờ cập nhật.

---

## Sáu module tri thức

| File | Nội dung |
|---|---|
| [`so-A-vai-tro-quy-trinh`](knowledge/so-A-vai-tro-quy-trinh.md) | Vai trò · quy trình 6 bước · **cổng A 8 ô** · cổng B · ba loại yêu cầu · ranh giới |
| [`so-B-tu-dien-doanh-so`](knowledge/so-B-tu-dien-doanh-so.md) | ★ **Cổng chặn** — bảy câu định nghĩa · luật cộng ngang · từ điển chỉ số marketing |
| [`so-C-bon-bao-cao`](knowledge/so-C-bon-bao-cao.md) | 6 loại báo cáo · trục và mốc mặc định · bẫy đặc trưng từng loại |
| [`so-D-phieu-order`](knowledge/so-D-phieu-order.md) | 14 trường · khuôn in cho người duyệt · vòng đời Order |
| [`so-E-nguon-du-lieu`](knowledge/so-E-nguon-du-lieu.md) | Nguồn · độ mịn · 3 rủi ro dữ liệu · **quyền riêng tư** |
| [`so-F-giao-tiep-tu-choi`](knowledge/so-F-giao-tiep-tu-choi.md) | Giọng · 5 tình huống nói không · mẫu tin nhắn |

---

## Quick start (4 bước)

1. Tạo 1 Project / GPT / Gem mới. Tên và mô tả: [`doc/01-cai-dat.md`](doc/01-cai-dat.md) §0.
2. **Instructions:** dán khối ▼▲ trong [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) — riêng **ChatGPT** dùng [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md) (6.896/8.000 ký tự).
3. **Knowledge:** upload 6 file [`knowledge/`](knowledge/) + 4 file [`prompts/`](prompts/) + [`template/mau-bao-cao-doanh-so.md`](template/mau-bao-cao-doanh-so.md).
4. Gõ câu lệnh tiếp nhận yêu cầu đầu tiên.

**Câu lệnh mẫu:**
```
Có yêu cầu báo cáo mới. Tiếp nhận giúp tôi.
NGƯỜI YÊU CẦU : Trưởng phòng Marketing — Kangnam
HỌ NÓI        : "Cho chị xem doanh số line Mũi tháng 10"
```
```
Chốt bảy câu định nghĩa cho báo cáo Doanh số MKT.
```

---

## Nửa tay — `tools/order.py`

```bash
python tools/order.py kiem    template/phieu-order.mau.json   # cổng A, 8 ô
python tools/order.py phieu   template/phieu-order.mau.json   # in phiếu bản người đọc
python tools/order.py bangiao template/phieu-order.mau.json   # gói bàn giao kỹ thuật
```

**Script tự chặn hai thứ:** cổng A chưa đủ 8 ô → ⛔ không bàn giao · người duyệt chưa ký (`ngay_duyet` trống) → ⛔ không bàn giao.

Nó cũng **cảnh báo** mà không chặn: mốc thời gian lệch mặc định của loại báo cáo · tiêu chí nghiệm thu không đếm được · tần suất *"một lần"* mà chưa ghi *không bảo trì* · phiếu có GIẢ ĐỊNH chưa ai đọc.

> ⛔ Script **không truy vấn dữ liệu và không dựng báo cáo**. Nó chỉ kiểm phiếu.

---

## ⚠️ Ranh giới cứng

- ⛔ **Agent không có dữ liệu và không được đoán số.** Ai hỏi một con số → chuyển người sở hữu số liệu.
- ⛔ **Không đưa dữ liệu định danh khách** (tên · SĐT · email · ảnh · bệnh án) vào báo cáo. Cần ví dụ thì dùng `KH-001`.
- ⚠️ Dịch vụ thẩm mỹ gắn với một người là **thông tin sức khoẻ**, không phải thông tin marketing thông thường.
- ⛔ **Không tự chốt định nghĩa thay Kế toán.** Agent đề xuất; người thật ký.
- ⛔ **Không im lặng làm hai bảng dùng hai định nghĩa khác nhau** cho cùng một chữ.

---

## Tài liệu
| File | Nội dung |
|---|---|
| [`doc/01-cai-dat.md`](doc/01-cai-dat.md) | Cài đặt · nạp tri thức · chạy thử 5 phút |
| [`doc/02-cau-lenh.md`](doc/02-cau-lenh.md) | Câu lệnh theo từng bước · lệnh `order.py` · khi agent trả lời sai |
| [`template/phieu-order.schema.json`](template/phieu-order.schema.json) | Schema 14 trường, máy đọc được |
| [`template/mau-bao-cao-doanh-so.md`](template/mau-bao-cao-doanh-so.md) | Mẫu 4 báo cáo dùng ở cổng B |
| [`doc/CHANGELOG.md`](doc/CHANGELOG.md) | Phiên bản · những gì chưa có |

---

*Agent soạn Order và trình. Người yêu cầu duyệt. Kỹ thuật dựng. Kế toán chốt định nghĩa. Bốn vai, không ai làm thay ai.*
"# Agent-Order-SoLieu" 
