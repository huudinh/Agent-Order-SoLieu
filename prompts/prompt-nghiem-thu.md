# PROMPT — NGHIỆM THU & RÀ SOÁT ĐỊNH KỲ

> Dùng sau khi kỹ thuật dựng xong, và mỗi quý một lần cho toàn bộ danh mục báo cáo.

---

## 1 · Nghiệm thu một báo cáo

```
Kỹ thuật đã dựng xong báo cáo theo phiếu [mã order].
Chạy nghiệm thu giúp tôi.

Với mỗi tiêu chí trong phiếu: ĐẠT / CHƯA ĐẠT / KHÔNG KIỂM ĐƯỢC.
Tiêu chí KHÔNG KIỂM ĐƯỢC phải nói rõ thiếu gì mới kiểm được.

Kiểm thêm ba thứ không nằm trong tiêu chí:
- Mặt bảng có đủ ba dòng định nghĩa chưa
- Con số tổng có khớp định nghĩa đã chốt không (đúng mốc, đúng gồm/trừ)
- Có chỗ nào dễ bị đem cộng ngang với báo cáo khác không
```

---

## 2 · Khi số không khớp

```
Báo cáo ra [số A], nhưng [người/hệ thống] nói là [số B]. Chênh [X]%.

Rà theo thứ tự này, đừng đổ lỗi trước:
① Hai bên có đang dùng CÙNG loại doanh số không? (ghi nhận / thực thu / đã thực hiện)
② CÙNG mốc thời gian không? (ngày chốt / thực hiện / thu tiền)
③ CÙNG quy tắc gồm-trừ không? (hoàn huỷ · chiết khấu · thẻ trả trước)
④ CÙNG phạm vi khách không?
⑤ Sau đó mới tới lỗi kỹ thuật.

Phần lớn chênh lệch dừng ở bước ① hoặc ②.
```

⚠️ **Đây là tình huống hay gặp nhất sau khi phát hành.** Bốn câu đầu giải thích được phần lớn chênh lệch — và nó **không phải lỗi của ai**, chỉ là hai định nghĩa khác nhau.

---

## 3 · Rà soát danh mục mỗi quý

```
Rà danh mục báo cáo đang chạy.

Với mỗi báo cáo:
- 3 tháng qua có ai mở không? Bao nhiêu lần?
- Quyết định ghi trong phiếu còn đúng không?
- Có trùng với báo cáo khác mới dựng không?
- Định nghĩa còn khớp với định nghĩa chung không?

Xếp thành ba nhóm: GIỮ · GỘP VÀO BÁO CÁO KHÁC · NGỪNG.
```

⚠️ **Dashboard không ai mở vẫn tốn công bảo trì** — và tệ hơn, nó vẫn chạy với định nghĩa cũ trong khi định nghĩa chung đã đổi. Một bảng sai nằm im nguy hiểm hơn một bảng không có.

---

## 4 · Khi người yêu cầu đổi ý sau khi đã duyệt

```
Phiếu [mã] đã duyệt và đang dựng, nhưng người yêu cầu muốn đổi [X].

⛔ Không sửa đè phiếu cũ. Mở phiên bản mới:
- Mã mới: [mã]-v2
- Ghi rõ đổi gì, vì sao, ai yêu cầu, ngày nào
- Nêu phần kỹ thuật đã làm có dùng lại được không

Rồi chạy lại cổng A cho bản v2.
```

⛔ **Sửa đè là cách mất dấu lý do.** Ba tháng sau không ai biết vì sao báo cáo tính theo cách đó, và sẽ có người đổi lại về cách cũ.
