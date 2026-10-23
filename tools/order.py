#!/usr/bin/env python3
"""order.py — nửa tay của Agent-Order-SoLieu.

Bộ não (prompt + knowledge) chạy trên Claude / ChatGPT / Gemini. Script này làm ba
việc mà một cuộc chat không làm chắc tay được: chạy cổng A bằng máy, in phiếu Order
ra bản người-đọc-được, và sinh gói bàn giao cho kỹ thuật.

    python tools/order.py kiem   <phieu.json>            # chạy cổng A, 8 ô
    python tools/order.py phieu  <phieu.json> [-o ra.md] # in phiếu bản người đọc
    python tools/order.py bangiao <phieu.json> [-o ra.md] # phiếu + nghiệm thu + chờ xác nhận

⛔ Script KHÔNG truy vấn dữ liệu và KHÔNG dựng báo cáo. Nó chỉ kiểm phiếu.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BAY_CAU = [
    ("loai_doanh_so", "Doanh số ghi nhận / thực thu / đã thực hiện"),
    ("moc_thoi_gian", "Tính theo ngày chốt / ngày thực hiện / ngày thu tiền"),
    ("gom_tru", "Gồm hay trừ: hoàn huỷ · chiết khấu · thẻ trả trước · trả góp · dịch vụ tặng"),
    ("tinh_ai", "Tính ai: khách mới / cũ / tái khám / walk-in"),
    ("quy_ve", "Quy về đơn vị nào"),
    ("vat", "Trước hay sau VAT"),
    ("da_dich_vu", "Khách dùng nhiều dịch vụ hoặc nhiều thương hiệu tính vào đâu"),
]

GOM_TRU = ["hoan_huy", "chiet_khau", "the_tra_truoc", "tra_gop", "dich_vu_tang"]

NHAN_DOANH_SO = {"ghi_nhan": "ghi nhận (đã ký, chưa cần thu đủ)",
                 "thuc_thu": "thực thu (tiền đã về)",
                 "da_thuc_hien": "đã thực hiện (dịch vụ làm xong)"}
NHAN_MOC = {"ngay_chot": "ngày chốt", "ngay_thuc_hien": "ngày thực hiện",
            "ngay_thu_tien": "ngày thu tiền"}
NHAN_QUY_VE = {"nguon_lead": "nguồn lead", "nhan_vien": "nhân viên", "co_so": "cơ sở",
               "thuong_hieu": "thương hiệu", "dich_vu": "dịch vụ"}
NHAN_LOAI = {
    "doanh-so-mkt": "① Doanh số MKT",
    "doanh-so-co-so": "② Doanh số Cơ sở",
    "doanh-so-thuong-hieu": "③ Doanh số Thương hiệu",
    "doanh-so-tap-doan": "④ Doanh số Tập đoàn",
    "doanh-so-dich-vu": "⑤ Doanh số dịch vụ",
    "ket-cau-doanh-so-mkt": "⑥ Kết cấu doanh số MKT",
    "khac": "Khác",
}
# Mốc mặc định của từng loại báo cáo — so-C. Lệch thì cảnh báo, không chặn.
# Báo cáo cắt theo KÊNH bắt buộc chốt câu 8 (quy gán nguồn) — so-B §1b.
BAO_CAO_CAN_CAU8 = ["doanh-so-mkt", "ket-cau-doanh-so-mkt"]
NHAN_QUY_GAN = {"cham_dau": "chạm đầu (kênh đầu tiên được tính)",
                "cham_cuoi": "chạm cuối (kênh cuối trước khi để lại số)",
                "chia_deu": "chia đều cho các kênh",
                "tat_ca": "tính cho TẤT CẢ các kênh"}
MOC_MAC_DINH = {
    "doanh-so-mkt": "ngay_chot",
    "doanh-so-co-so": "ngay_thuc_hien",
    "doanh-so-thuong-hieu": "ngay_thu_tien",
    "doanh-so-tap-doan": "ngay_thu_tien",
}
# Cụm từ không nghiệm thu được — nghiệm thu phải ĐẾM ĐƯỢC.
MO_HO = ["dễ nhìn", "chạy mượt", "đẹp", "trực quan", "thân thiện", "nhanh",
         "ổn định", "hợp lý", "đầy đủ thông tin"]


def doc(duong_dan: str) -> dict:
    p = Path(duong_dan)
    if not p.is_absolute():
        p = ROOT / p
    if not p.exists():
        loi(f"không thấy phiếu: {p}")
    return json.loads(p.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- cổng A

def cong_a(d: dict) -> list[tuple[str, bool, str]]:
    """Tám ô cổng A. Trả về [(mã, đạt, lý do)]."""
    ra = []

    # A1 — câu hỏi kinh doanh + quyết định đi kèm
    ch = (d.get("cau_hoi_kinh_doanh") or "").strip()
    qd = (d.get("quyet_dinh_di_kem") or "").strip()
    ra.append(("A1 có câu hỏi kinh doanh + quyết định đi kèm",
               bool(ch) and bool(qd),
               "" if ch and qd else "thiếu câu hỏi kinh doanh hoặc quyết định đi kèm"))

    # A2 — bảy câu định nghĩa, cộng câu 8 nếu là báo cáo kênh (① hoặc ⑥)
    dn = d.get("dinh_nghia") or {}
    thieu = [mo_ta for khoa, mo_ta in BAY_CAU if not dn.get(khoa)]
    if dn.get("gom_tru"):
        thieu_gt = [k for k in GOM_TRU if not dn["gom_tru"].get(k)]
        if thieu_gt:
            thieu.append("gồm/trừ còn thiếu: " + ", ".join(thieu_gt))
    can_cau8 = d.get("loai_bao_cao") in BAO_CAO_CAN_CAU8
    if can_cau8 and not dn.get("quy_gan_nguon"):
        thieu.append("CÂU 8 quy gán nguồn — báo cáo kênh bắt buộc có")
    nhan_a2 = "A2 đã chốt đủ BẢY CÂU định nghĩa" + (" + CÂU 8" if can_cau8 else "")
    ra.append((nhan_a2, not thieu,
               "còn thiếu — " + " · ".join(thieu) if thieu else ""))

    # A3 — mọi chỉ số có mẫu số
    cs = d.get("chi_so") or []
    thieu_ms = [c.get("ten", "?") for c in cs if not (c.get("mau_so") or "").strip()]
    ra.append(("A3 mọi chỉ số ghi rõ tử số và MẪU SỐ",
               bool(cs) and not thieu_ms,
               "chưa khai mẫu số: " + ", ".join(thieu_ms) if thieu_ms
               else ("chưa khai chỉ số nào" if not cs else "")))

    # A4 — nguồn dữ liệu có khai, và không còn CHỜ XÁC NHẬN ở tên bảng
    ng = d.get("nguon_du_lieu") or []
    cho = [n.get("he_thong", "?") for n in ng
           if "CHỜ XÁC NHẬN" in str(n.get("bang", ""))]
    ra.append(("A4 dữ liệu cần có TỒN TẠI trong hệ thống",
               bool(ng) and not cho,
               "chưa xác nhận tên bảng: " + ", ".join(cho) if cho
               else ("chưa khai nguồn dữ liệu" if not ng else "")))

    # A5 — độ mịn: chiều cắt phải khai
    cc = d.get("chieu_cat") or []
    ra.append(("A5 độ mịn dữ liệu đủ (đã khai chiều cắt)", bool(cc),
               "" if cc else "chưa khai chiều cắt nào"))

    # A6 — người sở hữu số liệu + người duyệt
    co_sh = any((n.get("nguoi_so_huu") or "").strip()
                and "CHỜ XÁC NHẬN" not in str(n.get("nguoi_so_huu"))
                for n in ng)
    co_duyet = bool((d.get("nguoi_duyet") or {}).get("ten"))
    ra.append(("A6 có người sở hữu số liệu + người duyệt", co_sh and co_duyet,
               "" if co_sh and co_duyet
               else ("thiếu người sở hữu số liệu" if not co_sh else "thiếu người duyệt")))

    # A7 — tần suất + hạn chót
    ts = (d.get("tan_suat") or {}).get("kieu")
    hc = (d.get("han_chot") or {}).get("ngay")
    ra.append(("A7 có tần suất + hạn chót", bool(ts) and bool(hc),
               "" if ts and hc else "thiếu tần suất hoặc hạn chót"))

    # A8 — không trùng báo cáo cũ (đã rà hay chưa)
    lq = d.get("bao_cao_lien_quan")
    ra.append(("A8 đã rà trùng với báo cáo đã có", lq is not None,
               "" if lq is not None else "chưa khai bao_cao_lien_quan — "
                                         "để [] nếu đã rà và không trùng"))
    return ra


def canh_bao(d: dict) -> list[str]:
    """Cảnh báo không chặn — nhưng phải in ra."""
    cb = []
    loai = d.get("loai_bao_cao")
    moc = (d.get("dinh_nghia") or {}).get("moc_thoi_gian")
    if loai in MOC_MAC_DINH and moc and moc != MOC_MAC_DINH[loai]:
        cb.append(f"Mốc thời gian '{NHAN_MOC.get(moc, moc)}' khác mặc định của "
                  f"{NHAN_LOAI.get(loai, loai)} là '{NHAN_MOC[MOC_MAC_DINH[loai]]}'. "
                  "Hợp lệ, nhưng phải in rõ lên mặt bảng và ⛔ không cộng ngang với "
                  "báo cáo khác mốc.")

    for n in d.get("nghiem_thu") or []:
        if any(m in n.lower() for m in MO_HO):
            cb.append(f"Tiêu chí nghiệm thu không đếm được: \"{n}\" — đổi thành một "
                      "phép so khớp có con số.")

    if (d.get("dinh_nghia") or {}).get("quy_gan_nguon") == "tat_ca":
        cb.append("Quy gán nguồn = 'tính cho TẤT CẢ các kênh' → tổng các bảng kênh sẽ "
                  "LỚN HƠN doanh số thật. Phải in cảnh báo 'không cộng ngang' lên mặt bảng.")

    if (d.get("tan_suat") or {}).get("kieu") == "mot_lan" \
            and "không bảo trì" not in str((d.get("tan_suat") or {}).get("ghi_chu", "")).lower():
        cb.append("Tần suất 'một lần' nhưng chưa ghi rõ KHÔNG BẢO TRÌ trong ghi_chu — "
                  "đây là cách một truy vấn một lần biến thành dashboard phải nuôi mãi.")

    if d.get("gia_dinh") and (d.get("nguoi_duyet") or {}).get("ngay_duyet"):
        cb.append(f"Phiếu có {len(d['gia_dinh'])} GIẢ ĐỊNH do agent tự đặt — "
                  "xác nhận người duyệt đã đọc phần đó, không chỉ đọc bảng.")

    if (d.get("trang_thai") == "DA_DUYET"
            and not (d.get("nguoi_duyet") or {}).get("ngay_duyet")):
        cb.append("Trạng thái DA_DUYET nhưng chưa có ngay_duyet — cổng B chưa qua.")
    return cb


# ---------------------------------------------------------------- in phiếu

def in_phieu(d: dict) -> str:
    dn = d.get("dinh_nghia") or {}
    gt = dn.get("gom_tru") or {}
    yc = d.get("nguoi_yeu_cau") or {}
    nd = d.get("nguoi_duyet") or {}
    r = []
    a = r.append

    a(f"# PHIẾU ORDER — {d.get('ma_order', '[chưa có mã]')}")
    a("")
    a(f"**Trạng thái:** `{d.get('trang_thai', 'NHAP')}` · **Ngày lập:** {d.get('ngay', '—')}")
    a("")
    a("| | |")
    a("|---|---|")
    a(f"| Người yêu cầu | {yc.get('ten', '—')} — {yc.get('bo_phan', '—')}"
      f"{' · ' + yc['thuong_hieu'] if yc.get('thuong_hieu') else ''} |")
    a(f"| Người duyệt | {nd.get('ten', '—')}"
      f"{' · duyệt ' + nd['ngay_duyet'] if nd.get('ngay_duyet') else ' · **chưa duyệt**'} |")
    a(f"| Loại báo cáo | {NHAN_LOAI.get(d.get('loai_bao_cao'), d.get('loai_bao_cao', '—'))} |")
    a(f"| Hạn chót | {(d.get('han_chot') or {}).get('ngay', '—')} · "
      f"ưu tiên {(d.get('han_chot') or {}).get('uu_tien', '—')} |")
    a("")
    a("## Câu hỏi kinh doanh")
    a(f"> {d.get('cau_hoi_kinh_doanh', '—')}")
    a("")
    a("**Quyết định đi kèm:** " + d.get("quyet_dinh_di_kem", "—"))
    a("")
    a("## Bảy câu định nghĩa đã chốt")
    a("")
    a("| Câu | Đã chốt |")
    a("|---|---|")
    a(f"| Loại doanh số | **{NHAN_DOANH_SO.get(dn.get('loai_doanh_so'), '⚠ chưa chốt')}** |")
    a(f"| Mốc thời gian | **{NHAN_MOC.get(dn.get('moc_thoi_gian'), '⚠ chưa chốt')}** |")
    a(f"| Hoàn huỷ | {gt.get('hoan_huy', '⚠ chưa chốt')} |")
    a(f"| Chiết khấu | {gt.get('chiet_khau', '⚠ chưa chốt')} |")
    a(f"| Thẻ trả trước | {gt.get('the_tra_truoc', '⚠ chưa chốt')} |")
    a(f"| Trả góp | {gt.get('tra_gop', '⚠ chưa chốt')} |")
    a(f"| Dịch vụ tặng | {gt.get('dich_vu_tang', '⚠ chưa chốt')} |")
    a(f"| Tính ai | {', '.join(dn.get('tinh_ai') or ['⚠ chưa chốt'])} |")
    a(f"| Quy về | {NHAN_QUY_VE.get(dn.get('quy_ve'), '⚠ chưa chốt')} |")
    a(f"| VAT | {'trước VAT' if dn.get('vat') == 'truoc_vat' else 'sau VAT' if dn.get('vat') else '⚠ chưa chốt'} |")
    a(f"| Đa dịch vụ / đa thương hiệu | {dn.get('da_dich_vu', '⚠ chưa chốt')} |")
    if d.get("loai_bao_cao") in BAO_CAO_CAN_CAU8:
        a(f"| ★ Quy gán nguồn *(câu 8)* | **{NHAN_QUY_GAN.get(dn.get('quy_gan_nguon'), '⚠ chưa chốt')}** |")
    a("")
    a("## Chỉ số")
    a("")
    a("| Chỉ số | Công thức | Tử số | **Mẫu số** | Đơn vị |")
    a("|---|---|---|---|---|")
    for c in d.get("chi_so") or []:
        a(f"| {c.get('ten', '—')} | {c.get('cong_thuc', '—')} | {c.get('tu_so', '—')} "
          f"| **{c.get('mau_so', '⚠ chưa khai')}** | {c.get('don_vi', '—')} |")
    a("")
    a("## Phạm vi & nguồn")
    pt = d.get("pham_vi_thoi_gian") or {}
    a(f"- **Chiều cắt:** {' · '.join(d.get('chieu_cat') or ['—'])}")
    a(f"- **Kỳ báo cáo:** {pt.get('ky_bao_cao', '—')}"
      + (f" · so với {pt['ky_so_sanh']}" if pt.get("ky_so_sanh") else ""))
    if pt.get("canh_bao_cung_loai_ky"):
        a(f"  - ⚠️ {pt['canh_bao_cung_loai_ky']}")
    ts = d.get("tan_suat") or {}
    a(f"- **Tần suất:** {ts.get('kieu', '—')}"
      + (f" · {ts['gio_cap_nhat']}" if ts.get("gio_cap_nhat") else "")
      + (f" · {ts['ghi_chu']}" if ts.get("ghi_chu") else ""))
    a("")
    a("| Hệ thống | Bảng | Người sở hữu | Độ trễ |")
    a("|---|---|---|---|")
    for n in d.get("nguon_du_lieu") or []:
        a(f"| {n.get('he_thong', '—')} | {n.get('bang', '—')} | "
          f"{n.get('nguoi_so_huu', '—')} | {n.get('do_tre', '—')} |")

    if d.get("gia_dinh"):
        a("")
        a("## ⚠️ GIẢ ĐỊNH AGENT TỰ ĐẶT")
        a("")
        a("> Người duyệt phải đọc phần này, không chỉ đọc bảng.")
        a("")
        for g in d["gia_dinh"]:
            a(f"- {g}")

    if d.get("rui_ro_du_lieu"):
        a("")
        a("## Rủi ro dữ liệu")
        for x in d["rui_ro_du_lieu"]:
            a(f"- {x}")

    if d.get("bao_cao_lien_quan"):
        a("")
        a("## Báo cáo liên quan")
        for x in d["bao_cao_lien_quan"]:
            a(f"- {x}")

    a("")
    a("## Tiêu chí nghiệm thu")
    for x in d.get("nghiem_thu") or []:
        a(f"- [ ] {x}")

    if d.get("cho_xac_nhan"):
        a("")
        a("## [CHỜ XÁC NHẬN]")
        a("")
        a("| Mục | Ai cấp | Chặn gì |")
        a("|---|---|---|")
        for c in d["cho_xac_nhan"]:
            a(f"| {c.get('muc', '—')} | {c.get('ai_cap', '—')} | {c.get('chan_gi', '—')} |")

    a("")
    a("---")
    a("> Ba dòng **bắt buộc in trên mặt báo cáo**: loại doanh số · mốc thời gian · "
      "phạm vi và nguồn. Thiếu ba dòng này thì bảng sẽ bị đem so với bảng khác định nghĩa.")
    return "\n".join(r) + "\n"


# ---------------------------------------------------------------- lệnh

def lenh_kiem(args) -> None:
    d = doc(args.phieu)
    o = cong_a(d)
    dat = sum(1 for _, ok, _ in o if ok)
    print(f"\nCỔNG A — {d.get('ma_order', '?')}\n" + "─" * 58)
    for ten, ok, vi_sao in o:
        print(f"  {'✓' if ok else '✗'}  {ten}")
        if not ok and vi_sao:
            print(f"       → {vi_sao}")
    print("─" * 58)
    print(f"  {dat}/8 ô ĐẠT")

    cb = canh_bao(d)
    if cb:
        print("\nCẢNH BÁO (không chặn, nhưng phải xử)")
        for x in cb:
            print(f"  ⚠  {x}")

    if dat < 8:
        print("\n⛔ CỔNG A CHƯA QUA — không chuyển kỹ thuật.")
        sys.exit(1)
    print("\n✓ Cổng A qua. Bước tiếp: in phiếu + mẫu báo cáo cho người yêu cầu duyệt (cổng B).")


def lenh_phieu(args) -> None:
    d = doc(args.phieu)
    noi_dung = in_phieu(d)
    xuat(noi_dung, args.o)


def lenh_bangiao(args) -> None:
    d = doc(args.phieu)
    o = cong_a(d)
    dat = sum(1 for _, ok, _ in o if ok)
    nd = d.get("nguoi_duyet") or {}
    if dat < 8:
        loi(f"cổng A mới {dat}/8 — ⛔ không bàn giao. Chạy `order.py kiem` để xem ô nào trượt.")
    if not nd.get("ngay_duyet"):
        loi("cổng B chưa qua — phiếu chưa có ngay_duyet của người duyệt. "
            "⛔ Không bàn giao khi người yêu cầu chưa xác nhận.")

    r = [in_phieu(d), "", "---", "", "## Gói bàn giao kỹ thuật", "",
         "| # | Phần | Trạng thái |", "|---|---|---|",
         "| ① | Phiếu Order 14 trường | ✓ ở trên |",
         "| ② | Mẫu báo cáo đã duyệt | ⚠ đính kèm riêng |",
         "| ③ | Tiêu chí nghiệm thu | ✓ ở trên |", "",
         f"**Người duyệt:** {nd.get('ten')} · {nd.get('ngay_duyet')} "
         f"· {nd.get('hinh_thuc', '—')}", "",
         "> ⛔ Đổi yêu cầu sau khi đã duyệt thì **mở phiếu mới `-v2`**, không sửa đè phiếu này."]
    cb = canh_bao(d)
    if cb:
        r += ["", "### ⚠️ Cảnh báo chuyển kèm cho kỹ thuật"] + [f"- {x}" for x in cb]
    xuat("\n".join(r) + "\n", args.o)


def xuat(noi_dung: str, duong_dan: str | None) -> None:
    if duong_dan:
        p = Path(duong_dan)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(noi_dung, encoding="utf-8")
        print(p)
    else:
        print(noi_dung)


def loi(msg: str):
    print(f"⛔ {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    for luong in (sys.stdout, sys.stderr):
        try:
            luong.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass

    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="lenh", required=True)

    p = sub.add_parser("kiem", help="chạy cổng A, 8 ô")
    p.add_argument("phieu")
    p.set_defaults(func=lenh_kiem)

    p = sub.add_parser("phieu", help="in phiếu Order bản người đọc")
    p.add_argument("phieu")
    p.add_argument("-o")
    p.set_defaults(func=lenh_phieu)

    p = sub.add_parser("bangiao", help="gói bàn giao kỹ thuật (cần qua cả hai cổng)")
    p.add_argument("phieu")
    p.add_argument("-o")
    p.set_defaults(func=lenh_bangiao)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
