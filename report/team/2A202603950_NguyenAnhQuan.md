# Báo cáo cá nhân — NguyenAnhQuan-2A202603950

## 1. Thông tin thành viên

- Họ tên: Nguyễn Anh Quân
- MSSV: 2A202603950
- Email: anhhquan511@gmail.com
- GitHub: anhhquan511
- Vai trong nhóm: Người kiểm số — Người 2 trong [PHAN_CONG.md](../../PHAN_CONG.md). Phụ trách kiểm số độc lập A1–A2, Nhiệm vụ B (B1–B4) và rủi ro kinh tế E2.

## 2. Phần việc phụ trách

- Kiểm số độc lập A1 và A2 bằng `pandas` (không phụ thuộc code Người 1) để đối chiếu kết quả mô hình chi phí.
- **CP2 · Nhiệm vụ B (B1–B4):** viết module [src/cp2_do_nhay.py](../../src/cp2_do_nhay.py) nhận `mo_hinh` làm tham số (có bản tạm để chạy độc lập trước khi merge và tự chuyển sang `lab13.mo_hinh` sau khi Người 1 hoàn thiện) và điền mục B1–B4 trong [report/team/bang_chi_phi.md](bang_chi_phi.md).
- **CP5 · Nhiệm vụ E2:** xây dựng bảng rủi ro kinh tế trong [report/team/chi_so.md](chi_so.md) dựa trực tiếp trên các con số độ nhạy đã tính.
- Duyệt chéo Gate 2a: cùng Người 1 chấm hồ sơ nhóm bạn vào [report/team/phieu_cham.md](phieu_cham.md).

## 3. Đóng góp cụ thể

- **Kiểm số độc lập A1–A2 (`kiem_tra_a1_a2_doc_lap`):** tính trực tiếp bằng công thức phân phối hình học (`1,20 · 1,25 · 1,25`) và tổng hợp `pandas` trực tiếp trên `logix_runs.csv` và `logix_requests.csv`; xác nhận khớp 100% với `lab13.mo_hinh` của Người 1.
- **B1 (9 kịch bản độ nhạy):** tính đầy đủ 9 kịch bản thay đổi giá token, tỉ lệ xem lại, số ca làm lại, lương nhân viên và giới hạn số lần chạy (`1`, `2` lần); tích hợp `assert` tự kiểm tra mức giảm của kịch bản "giảm một nửa" bằng đúng 1/2 mức tăng của kịch bản "gấp đôi".
- **B2 (đổi một cặp và xếp hạng):** tính kịch bản `Giá token ×2 + Tỉ lệ xem lại ×2` ra **6.543 đ (`+46,3%`, `simulated`)**, xác nhận cộng tuyến tính (`+5,6% + 40,7% = +46,3%`) và xếp hạng 3 yếu tố nhạy nhất: **1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên**.
- **B3 (chi phí cả hệ thống theo giới hạn chạy lại):** tính chi phí cả hệ thống (`tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công`) cho 1, 2 và 3 lần chạy; chứng minh giới hạn **2 lần** rẻ nhất cho công ty (**6.901.220 đ**, `simulated`) dù CPS thấp nhất nằm ở **1 lần** (**4.111 đ**, `simulated`, đẩy thêm **85 ca** sang nhân viên).
- **B4 (xem lại 100% trong phạm vi `noi_dia` + `hang_nang`):** tính cả hai trường hợp — giả định 9 phút làm lại (**11.743 đ = 0,98×**, hoà vốn ≤ **5,1 phút**/lần xem lại) và trung bình thực tế `15,3 phút`/ca từ `phut_lam_lai_simulated` (**12.415 đ = 1,03×**, hoà vốn ≤ **4,8 phút**/lần xem lại, đắt hơn nhân viên tự làm).
- **E2 (rủi ro kinh tế):** viết 3 dòng rủi ro định lượng (làm lại ×2, xem lại 100% kéo dài, khối lượng thấp làm tăng chi phí cố định mỗi việc) kèm dấu hiệu theo dõi, hành động cụ thể và vai trò phụ trách (`PM trợ lý hoàn phí`, `Trưởng nhóm CSKH`, `Giám đốc vận hành`).

## 4. Bằng chứng

- Nhánh `p2-B`, commit `2599b35` ("feat(p2-B): independent A1-A2 check, CP2 sensitivity B1-B4, and E2 economic risks"), đã merge vào `main` tại commit `994a3ff` và nối vào `src/lab13.py` tại commit `3918943`.
- File đã tạo/cập nhật: [src/cp2_do_nhay.py](../../src/cp2_do_nhay.py), [report/team/bang_chi_phi.md](bang_chi_phi.md) (B1–B4), [report/team/chi_so.md](chi_so.md) (E2), [TEAM.md](../../TEAM.md).
- Lệnh kiểm tra: `cd src && python cp2_do_nhay.py` (dùng trực tiếp `lab13.mo_hinh`, đối chiếu A2 khớp 100%, qua toàn bộ `assert`) và `cd src && python lab13.py`.
- Con số chính do tôi tính:

| Hạng mục | Giá trị | Nhãn |
| --- | ---: | --- |
| Đối chiếu A2: CPS / gấp hoá đơn mỗi yêu cầu | 4.472 đ / 16,3× | simulated |
| B1: Số ca làm lại ×2 / Xem lại ×2 / Lương +25% | +51,8% / +40,7% / +23,1% | simulated |
| B1: Giá token ×2 / giảm một nửa | +5,6% / −2,8% | simulated |
| B2: Giá token ×2 + Xem lại ×2 | 6.543 đ (+46,3%) | simulated |
| B3: Chi phí cả hệ thống 1 / 2 / 3 lần chạy | 7.449.781 / **6.901.220** / 7.037.585 đ | simulated |
| B4: Xem lại 100% (9 phút làm lại) / hoà vốn xem lại | 11.743 đ (0,98×) / ≤ 5,1 phút | simulated |
| B4: Xem lại 100% (15,3 phút TB dữ liệu) / hoà vốn xem lại | 12.415 đ (1,03×) / ≤ 4,8 phút | simulated |

## 5. Công cụ AI đã dùng

- **Antigravity (trợ lý AI dùng mô hình Gemini):** dùng để đọc yêu cầu phân công, gợi ý cấu trúc module `src/cp2_do_nhay.py`, định dạng bảng markdown cho B1–B4 và E2, và rà soát quy tắc lab.
- **Cách tôi tự kiểm tra kết quả:**
  - Chạy `cd src && python cp2_do_nhay.py` và `cd src && python lab13.py` sau khi merge `main`: xác nhận `cp2_do_nhay.py` gọi trực tiếp `lab13.mo_hinh` và khớp 100% với hàm tính độc lập bằng `pandas`.
  - Kiểm tra tự động bằng `assert`: các kịch bản "giảm một nửa" giảm đúng bằng 1/2 mức tăng của kịch bản "gấp đôi"; kịch bản cặp B2 bằng đúng tổng hai tác động riêng.
  - Đối chiếu từng con số B1–B4 với số tham chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 0,1%, xa trong ngưỡng 2%).
  - Kiểm tra nhãn `simulated` cho mọi số xuất phát từ cột `*_simulated`, độ dài câu trả lời ≤ 3 dòng, vai phụ trách cụ thể và không xuất hiện từ cấm.

## 6. Tự đánh giá

- **Làm được:** hoàn thành đầy đủ kiểm số A1–A2, B1–B4, E2 đúng chuẩn tách module để merge vào `main` không xung đột; tất cả số liệu đều được sinh ra từ code và qua kiểm tra chéo với Người 1.
- **Điều rút ra:**
  - Giá token chỉ làm CPS thay đổi `+5,6%` khi tăng gấp đôi, trong khi làm lại (`+51,8%`) và xem lại (`+40,7%`) mới là đòn bẩy kinh tế chính cần theo dõi trong pilot.
  - Tối ưu riêng CPS (giới hạn 1 lần: `4.111 đ`) gây phản tác dụng ở cấp công ty vì đẩy thêm 85 ca sang nhân viên; chi phí cả hệ thống mới phản ánh đúng bài toán kinh tế (rẻ nhất ở giới hạn 2 lần: `6.901.220 đ`).
  - Nếu buộc xem lại 100%, tiền xem lại chiếm tới `89,7%` chi phí và triệt tiêu lợi ích tiết kiệm (thậm chí đắt hơn nhân viên tự làm `1,03×` khi tính theo 15,3 phút làm lại thực tế), nên pilot bắt buộc phải có lộ trình hạ tỉ lệ xem lại an toàn.
- **Cần cải thiện:** chủ động thống nhất sớm hơn với cả nhóm về tên các vai phụ trách và hoàn thành phần duyệt chéo `phieu_cham.md` đúng mốc 17:00.
