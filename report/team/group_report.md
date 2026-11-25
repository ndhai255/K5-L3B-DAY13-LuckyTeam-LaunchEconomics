# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: LuckyTeam
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Mục tiêu của bài lab là định giá trợ lý hoàn phí LogiX-VN từ dữ liệu trace chạy thử (1.200 yêu cầu, 1.624 lần chạy) và lập bộ hồ sơ launch v0 cho hội đồng duyệt chéo Gate 2a nhằm trả lời bốn câu hỏi: chi phí thực mỗi việc thành công có đáng chạy không, nhân viên có dùng không, khi lỗi xảy ra thì phát hiện/khắc phục thế nào, và kế hoạch pilot phải thiết kế ra sao để tách được tác động.

Nhóm phân công 4 thành viên làm song song theo [PHAN_CONG.md](../../PHAN_CONG.md): mỗi người giữ module code và file báo cáo riêng trên nhánh riêng (`p1-A`, `p2-B`, `p3-CD`, `p4-E`), gắn nhãn lỗi độc lập rồi mới so đồng thuận ở nhiệm vụ C, sau đó merge về `main` để chốt số vào hồ sơ Gate 2a.

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** kiểm tra 3 phép thử đáp án biết trước, xây dựng `mo_hinh` tính chi phí mỗi việc thành công (tử số tính mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `thanh_cong`), tách theo 4 loại yêu cầu và cộng chi phí cố định 40 triệu đ/tháng. Chi tiết: [bang_chi_phi.md](bang_chi_phi.md), `src/lab13.py`.
- **Nhiệm vụ B (Phân tích độ nhạy):** chạy 9 kịch bản đổi từng yếu tố, 1 kịch bản đổi cặp, so sánh chi phí cả hệ thống theo giới hạn 1/2/3 lần chạy và kiểm tra kịch bản xem lại 100% cho `noi_dia` + `hang_nang`. Chi tiết: [bang_chi_phi.md](bang_chi_phi.md), `src/cp2_do_nhay.py`.
- **Nhiệm vụ C (Phân loại lỗi & khắc phục):** hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR (theo nguyên nhân gốc), so tỉ lệ đồng thuận, ghi quy tắc cho các ca lệch và lập bảng khắc phục 5 ca đủ 5 loại. Chi tiết: [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** tính cỡ mẫu và hệ số thiết kế cho 3 cách chia (theo yêu cầu, theo nhân viên, theo depot), đánh giá 5 câu hỏi tách tác động và viết luật dừng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ. Chi tiết: [pilot_plan.yaml](pilot_plan.yaml), `src/cp4_co_mau.py`.
- **Nhiệm vụ E (Chỉ số, event, rủi ro & hồ sơ Gate 2a):** tính 3 chỉ số E1 từ `src/logix_requests.csv` bằng `src/cp5_chi_so.py`, đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, đặc tả 10 event có `trace_id` kèm kiểm tra chéo, tổng hợp rủi ro kinh tế từ bài B và đóng gói hồ sơ một trang 7 mục. Chi tiết: [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md), [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Mô hình chi phí (A1–A4):** qua cả 3 phép thử A1 (1,20 · 1,25 · 1,25). Chi phí mỗi việc thành công là **4.472 đ** (`simulated`), gấp **16,3 lần** hoá đơn token + tool (274,7 đ/yc); làm lại chiếm 51,8% và xem lại 40,7%. Chi phí cả hệ thống (gồm 222 ca nhân viên làm thay) là **5.865 đ/yc = 0,49×** của 12.000 đ (`simulated`). Phạm vi pilot `noi_dia` (0,22×) + `hang_nang` (0,69×), loại `quoc_te` (1,88×, tỉ lệ ok tụt 30,0% → 11,4% → 2,2%) và `doi_tac` (0,85×). Cộng cố định 40 triệu đ/tháng: **4.599 đ = 0,38×** ở 45.000 yc/tháng và **5.784 đ = 0,48×** ở 1/2 khối lượng (`simulated`).
- **Độ nhạy và rủi ro kinh tế (B1–B4, E2):** top 3 yếu tố nhạy nhất là số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) (`simulated`). Giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (**6.901.220 đ**, `simulated`). Nếu phải xem lại 100% trong phạm vi pilot (B4), chi phí tăng lên **11.743 đ = 0,98×** (9 phút làm lại) hoặc **12.415 đ = 1,03×** (15,3 phút thực tế, `simulated`), đòi hỏi lộ trình giảm xem lại theo bậc.
- **Chỉ số đợt chạy thử (E1, 1.200 yêu cầu):**
  - Chỉ số chính (% đóng trong 24 giờ và không mở lại trong 7 ngày): **82,83%** (994/1.200); trong phạm vi `noi_dia` + `hang_nang`: **92,26%** (906/982).
  - Chỉ số dùng (tỉ lệ bỏ qua gợi ý): **27,12%** (48/177); trong phạm vi pilot: **21,09%** (27/128).
  - Chỉ số an toàn (tỉ lệ lỗi lọt đến khách — mở lại 7 ngày): **4,25%** (51/1.200); trong phạm vi pilot: **3,97%** (39/982).
- **Bảng lỗi và pilot plan (C–D):** Hai bộ nhãn độc lập trùng **18/20 = 90%**; ca 12 thống nhất **Ngầm**, ca 13 **Giới hạn hệ thống**, kèm bảng khắc phục đủ năm loại. Pilot chỉ gồm `noi_dia` + `hang_nang`, random theo staff 20 can thiệp/20 đối chứng; chấp nhận MDE 6 điểm, cần **5.980** yêu cầu thô tương đương **859** mẫu hiệu dụng mỗi nhánh (DE 6,96). **Con số bất lợi:** nếu tác động thật chỉ 5 điểm thì power chỉ còn **0,64**. Rollout 10% → 25% → 50%, quyết định đề xuất T+37, có bốn luật dừng (hoàn trùng, mở lại 7 ngày, CPS > 8.000 đ, bỏ qua gợi ý > 40%) và rollback. `python lab13.py` in đủ A, B, D1 và E1.
- **Đề xuất Gate 2a:** **Go có điều kiện** cho pilot `noi_dia` + `hang_nang` (chi tiết 4 điều kiện, người phụ trách và ngày kiểm tra tại [ho_so_launch_v0.md](ho_so_launch_v0.md)).
- **Duyệt chéo hội đồng:** lớp L3B lẻ nhóm nên không có nhóm hội đồng chấm chéo. Nhóm **tự rà soát** theo rubric Gate 2a: **30/30**, **Go có điều kiện** (chi tiết tại [phieu_cham.md](phieu_cham.md); đây không phải điểm của nhóm khác). Đạt đủ 10/10 ở cả 3 tiêu chí: đề xuất khớp bằng chứng và nêu rõ con số bất lợi (B4 lên 1,03×, power 0,64 ở 5 điểm), mọi số giả lập đều có nhãn `simulated`, và pilot tách được tác động theo staff 20 + 20 với 4 luật dừng định lượng.

## 5. Khó khăn và cách xử lý

- **Rủi ro xung đột khi 4 người làm song song:** xử lý bằng cách tách code B, D, E ra các module riêng (`cp2_do_nhay.py`, `cp4_co_mau.py`, `cp5_chi_so.py`) và chia quyền sở hữu file theo từng mục.
- **Đọc dữ liệu CSV bị lỗi `NaN`:** cột `quyet_dinh_xem_lai` có ô trống cho các yêu cầu không xem lại; nhóm thống nhất dùng `pd.read_csv(..., keep_default_na=False)` trong mọi script.
- **Dữ liệu thời gian nhân viên là giả lập (`_simulated`):** mọi con số chi phí phụ thuộc hai cột này đều gắn nhãn `simulated` và được đưa vào điều kiện thay bằng đo thật (`phut_xem_lai_thuc`, `phut_lam_lai_thuc`) sau tuần 1 pilot.
- **Đợt chạy thử không có nhóm đối chứng:** nhóm diễn giải chặt chẽ là "chỉ số trong đợt chạy thử là 82,83%", không khẳng định trợ lý đã nâng chỉ số.

## 6. Tổng hợp đóng góp

Chi tiết phân vai, đóng góp và bằng chứng của từng thành viên nằm trong [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện là dữ liệu `simulated`; cần thu thập từ event `staff_review_decision` và `staff_rework_completed` ngay tuần đầu pilot để tính lại chi phí thực.
- Các lỗi ngầm (như hoàn sai tiền do bảng giá cũ hoặc mã giảm giá) không tạo yêu cầu mở lại; cần duy trì kiểm tra mẫu 100 đơn/tuần qua event `audit_sample_checked` và đối soát sổ cái hằng giờ.
- Khi thiết kế pilot chia cụm theo nhân viên với 40 nhân viên, cần theo dõi sát rủi ro tràn tác động trong cùng depot và kiểm soát lộ trình giảm tỉ lệ xem lại để đảm bảo hiệu quả kinh tế.

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn buổi chiều Lab 13 (`docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).
- Tài liệu dữ liệu và công thức (`docs/du_lieu_va_cong_thuc.md`).
- Phân loại lỗi hệ thống AI theo khung Google PAIR (5 loại: Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Ngầm).
