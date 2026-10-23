# 01 — CÀI ĐẶT (15 phút)

Agent có **hai nửa**:
- **Nửa não** — prompt + knowledge, chạy trên Claude / ChatGPT / Gemini. Không cần cài gì lên máy.
- **Nửa tay** — `tools/order.py`, chạy cổng A bằng máy và in phiếu Order. Cần Python, không cần thư viện ngoài.

---

## 0. Ba ô phải điền khi tạo agent mới

**Tên**
```
Agent-Order-SoLieu
```

**Mô tả** — 262 ký tự, dưới trần 300 của ChatGPT:
```
Tiếp nhận yêu cầu báo cáo từ phòng Marketing, các thương hiệu và tập đoàn lên Team Số liệu HCI. Hỏi cho rõ mục tiêu, chốt bảy câu định nghĩa doanh số, dựng mẫu báo cáo để duyệt, rồi ra Phiếu Order đủ để kỹ thuật dựng ngay. Không dựng dashboard, không đoán số.
```

**Câu mở đầu hội thoại**
```
Có yêu cầu báo cáo mới. Tiếp nhận giúp tôi.
```
```
Chốt bảy câu định nghĩa cho báo cáo Doanh số MKT.
```

---

## 1. Nạp bộ não

| Nền tảng | Dán vào đâu | Dùng file nào |
|---|---|---|
| **Claude Project** | *Custom instructions* | [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md), khối giữa hai vạch ▼▲ |
| **ChatGPT Custom GPT** | *Instructions* (trần 8.000) | [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) — hiện **6.896** ký tự |
| **Gemini Gem** | *Chỉ dẫn* | `SYSTEM-PROMPT.md` |
| **Claude Code** | `CLAUDE.md` hoặc dán vào chat | `SYSTEM-PROMPT.md` |

## 2. Nạp tri thức — 11 file

```
knowledge/so-A-vai-tro-quy-trinh.md     prompts/prompt-tiep-nhan.md
knowledge/so-B-tu-dien-doanh-so.md      prompts/prompt-chot-dinh-nghia.md
knowledge/so-C-bon-bao-cao.md           prompts/prompt-ra-order.md
knowledge/so-D-phieu-order.md           prompts/prompt-nghiem-thu.md
knowledge/so-E-nguon-du-lieu.md         template/mau-bao-cao-doanh-so.md
knowledge/so-F-giao-tiep-tu-choi.md
```

Nền tảng chặn số file (Gemini Gems: 10) → dùng bản gộp `goi/GOP-tri-thuc.md` thay cho 6 file `knowledge/`.
Sinh lại sau mỗi lần sửa: `python tools/gop-tham-khao.py`. ⛔ Đừng sửa tay file gộp.

---

## 3. Cài nửa tay

Không cần thư viện ngoài:
```bash
python tools/order.py kiem template/phieu-order.mau.json
```

Phiếu mẫu **cố ý trượt ô A4** (chưa xác nhận tên bảng) để thấy cổng chặn hoạt động:
```
✗  A4 dữ liệu cần có TỒN TẠI trong hệ thống
     → chưa xác nhận tên bảng: Meta Ads, Google Ads, CRM Caresoft
⛔ CỔNG A CHƯA QUA — không chuyển kỹ thuật.
```

**Thử cổng B:** chạy `order.py bangiao` trên phiếu mẫu — script phải **từ chối**, vì cổng A chưa qua và người duyệt chưa ký. Từ chối đúng là cổng còn sống.

---

## 4. ⚠️ Ba việc phải làm trước khi dùng thật

| # | Việc | Ai | Chặn gì nếu thiếu |
|---|---|---|---|
| 1 | **Chốt bảy câu định nghĩa dùng chung** cho toàn tập đoàn, bằng văn bản | Team Số liệu + Kế toán | Agent vẫn chạy, nhưng phải hỏi lại **từng ca** — và hai phòng vẫn ra hai số khác nhau |
| 2 | Điền **bảng nguồn dữ liệu** trong `knowledge/so-E` — hệ thống, bảng, người sở hữu, độ trễ | Team Số liệu | Ô **A4** cổng A luôn trượt |
| 3 | Lập **danh mục báo cáo đang chạy** | Team Số liệu | Ô **A8** không rà trùng được |

> **Việc 1 là việc có đòn bẩy cao nhất của cả gói.** Chốt một lần, dùng cho mọi báo cáo về sau — và nó cắt đứt loại tranh cãi tốn nhiều thời gian nhất giữa Marketing, Cơ sở và Kế toán.

---

## 5. Thứ tự triển khai đề xuất

1. **Tuần 1** — cài agent, chạy thử trên 2–3 yêu cầu có thật nhưng chưa gấp.
2. **Tuần 2** — dùng chính agent để chốt bảy câu định nghĩa dùng chung; đưa Kế toán duyệt.
3. **Tuần 3** — điền bảng nguồn dữ liệu, lập danh mục báo cáo đang chạy.
4. **Tuần 4+** — mọi yêu cầu báo cáo mới đi qua agent. Rà soát danh mục mỗi quý.
