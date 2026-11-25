# Báo cáo cá nhân — NguyenDucHai-2A202603943

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Hải
- MSSV: 2A202603943
- Email: ndhai255.work@gmail.com
- Vai trong nhóm: Người viết code (trước giải lao), Người 1 trong [PHAN_CONG.md](../../PHAN_CONG.md). Phụ trách nhiệm vụ A và nối các module vào `src/lab13.py` cuối buổi.

## 2. Phần việc phụ trách

- **CP1 · Nhiệm vụ A**: mô hình chi phí mỗi việc thành công trong `src/lab13.py` (A1–A4).
- Phần A1–A4 của `report/team/bang_chi_phi.md`.
- Merge các nhánh `p1-A` → `p2-B` → `p3-CD` → `p4-E`, nối `cp2_do_nhay`, `cp4_co_mau`, `cp5_chi_so` vào `__main__` để `python lab13.py` chạy hết từ đầu đến cuối.
- Duyệt chéo Gate 2a: cùng Người 2 chấm hồ sơ nhóm bạn vào `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **A1:** viết ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; qua ba phép thử 1,20 · 1,25 · 1,25. Hệ số chi phí = E[số lần chạy] ÷ P(thành công) = 1/p, không phụ thuộc k.
- **A2:** viết `mo_hinh(runs, reqs, …)`: tử số cộng token + tool của **mọi** lần chạy kể cả lần lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Có nhánh `max_lan_chay` cho B1, B3 và trả thêm `chay_lai`, `hoa_don_moi_yc` để Người 2 gọi lại ở bài B.
- **A3:** viết `tach_theo_loai` (gọi lại `mo_hinh` cho từng `loai`) và `ti_le_ok_theo_lan_chay` (tỉ lệ `status = ok` theo `attempt`) để trả lời câu "chạy lại có giúp không".
- **A4:** viết `chi_phi_co_dinh` cộng 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`, ở 45.000 yêu cầu/tháng và một nửa khối lượng.
- Điền bảng A1, A2, A3, A4 và các câu trả lời vào `bang_chi_phi.md`, ghi nhãn `simulated` cho mọi số dùng cột `_simulated`.
- Viết A3, A4 thành hàm riêng (không viết thẳng trong `__main__`) để các module khác import lại được.

## 4. Bằng chứng

- Commit `5e91a4b` trên nhánh `p1-A`: "A1-A4: cost-per-success model, split by loai, fixed cost".
- File: [src/lab13.py](../../src/lab13.py), [report/team/bang_chi_phi.md](bang_chi_phi.md) (mục A1–A4).
- Lệnh `cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và các bảng A2, A3, A4.
- Con số chính do tôi tính:

| Chỉ số | Giá trị | Nhãn |
| --- | ---: | --- |
| Chi phí mỗi việc thành công (A2) | 4.472 đ | simulated |
| Gấp hoá đơn token + tool chia số yêu cầu (274,7 đ) | 16,3 lần | simulated |
| Tỉ trọng làm lại / xem lại trong tổng chi phí | 51,8% / 40,7% | simulated |
| Chi phí cả hệ thống mỗi yêu cầu, gồm 222 ca nhân viên làm thay | 5.865 đ = 0,49× | simulated |
| quoc_te: chi phí mỗi việc thành công | 22.515 đ = 1,88× | simulated |
| quoc_te: tỉ lệ ok lần 1 → 2 → 3 | 30,0% → 11,4% → 2,2% | đo từ trace |
| A4: noi_dia + hang_nang + cố định, 45.000 yc/tháng | 4.599 đ = 0,38× | simulated |
| A4: như trên, một nửa khối lượng | 5.784 đ = 0,48× | simulated |

## 5. Công cụ AI đã dùng

- **Claude Code** (trong VS Code): đọc đề và `PHAN_CONG.md` để tóm tắt việc của Người 1, viết code A1–A4 vào `src/lab13.py`, điền phần A1–A4 trong `bang_chi_phi.md` và soạn nháp báo cáo này.
- **Cách tôi kiểm tra:**
  - Chạy `python lab13.py`: ba phép thử A1 in ĐẠT.
  - So từng số A2, A3, A4 với số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: tất cả khớp, lệch dưới 2%.
  - Phát hiện một bẫy ở A4: phải chia cho 1.200 yêu cầu của cả mẫu (vì 45.000 là khối lượng cả công ty), không chia cho 982 yêu cầu trong phạm vi. Chia sai cho ra 0,37× thay vì 0,38×.
  - Đối chiếu số A2 với số Người 2 tính độc lập bằng pandas.

## 6. Tự đánh giá

- **Làm được:** mô hình A chạy đúng, qua ba phép thử, số khớp đáp án; `mo_hinh` có sẵn tham số cho bài B nên Người 2 chỉ cần gọi lại.
- **Điều rút ra:**
  - Chi phí thật của trợ lý nằm ở giờ nhân viên (92,5% tổng chi phí), không phải ở token. Chỉ nhìn hoá đơn token là đánh giá thấp chi phí 16 lần.
  - Chạy lại chỉ có ích khi lỗi là ngẫu nhiên. Với `quoc_te`, lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền; nên loại khỏi phạm vi pilot.
  - So với 12.000 đ phải dùng chi phí cả hệ thống (0,49×), không dùng 4.472 đ (0,37×), vì 4.472 đ chưa tính phần nhân viên làm thay.
- **Cần cải thiện:** thống nhất sớm hơn quy ước đọc CSV (`keep_default_na=False`) và giao diện hàm giữa các module để ghép nhánh `p1-A` → `p4-E` vào `src/lab13.py` kịp mốc 17:00 trước phiên duyệt chéo Gate 2a.
