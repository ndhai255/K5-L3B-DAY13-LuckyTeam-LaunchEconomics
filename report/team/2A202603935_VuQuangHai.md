# Báo cáo cá nhân — VuQuangHai-2A202603935

## 1. Thông tin thành viên

- Họ tên: Vũ Quang Hải
- MSSV: 2A202603935
- Email: haivq25@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ, Người 4 trong [PHAN_CONG.md](../../PHAN_CONG.md). Phụ trách gắn nhãn độc lập 20 ca lỗi (CP3), nhiệm vụ E1 và danh sách event (`chi_so.md`), dựng và tổng hợp hồ sơ Gate 2a (`ho_so_launch_v0.md`), `TEAM.md` và `group_report.md`.

## 2. Phần việc phụ trách

- **CP3 · Nhiệm vụ C (Nhãn 2):** gắn nhãn độc lập 20 ca lỗi từ đề bài theo 5 loại Google PAIR để so đồng thuận với Người 3.
- **CP5 · Nhiệm vụ E1 & Event:** viết module `src/cp5_chi_so.py` tính 3 chỉ số (chính, dùng, an toàn) từ `src/logix_requests.csv`; đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn; liệt kê ít nhất 6 event có `trace_id` và kiểm tra chéo với bảng chỉ số trong `report/team/chi_so.md`.
- **Giữ hồ sơ Gate 2a:** dựng khung 7 mục ngay từ đầu và điền số sau khi các nhánh merge vào `report/team/ho_so_launch_v0.md`; cập nhật `TEAM.md` và `report/team/group_report.md`.
- **Duyệt chéo Gate 2a:** cùng Người 3 bảo vệ hồ sơ nhóm trước hội đồng.

## 3. Đóng góp cụ thể

- **Gắn nhãn độc lập 20 ca lỗi:** phân loại toàn bộ 20 ca theo nguyên nhân gốc (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm) và đối chiếu với Người 3 đạt đồng thuận **18/20 = 90%** (ca 12 thống nhất Ngầm, ca 13 thống nhất Giới hạn hệ thống trong [bang_loi.md](bang_loi.md)).
- **Viết `src/cp5_chi_so.py`:** thiết kế hàm `tinh_chi_so_e1(reqs)` và `chay_chi_so(reqs)` tách thành module riêng để Người 1 import trực tiếp vào `src/lab13.py` mà không xung đột merge; đọc `logix_requests.csv` với `keep_default_na=False`.
- **Hoàn thiện E1 và 10 event trong `report/team/chi_so.md`:** tính đủ 3 chỉ số trên 1.200 yêu cầu và tham chiếu trên phạm vi pilot (`noi_dia` + `hang_nang`); đề xuất thêm *Tỉ lệ tiếp nhận sử dụng trợ lý* (dùng) và *Tỉ lệ đơn hoàn sai tiền hoặc hoàn trùng qua kiểm tra mẫu hằng tuần* (an toàn); thiết kế 10 event có `trace_id` đo được 100% các chỉ số E1 và thay hai cột phút `simulated` bằng dữ liệu đo thật sau tuần 1.
- **Tổng hợp hồ sơ và báo cáo nhóm:** dựng và hoàn thiện [ho_so_launch_v0.md](ho_so_launch_v0.md) đủ 7 mục (số liệu A–E, nhãn `simulated`, con số bất lợi B4 và đánh đổi MDE 6 điểm / power 0,64, đề xuất **Go có điều kiện**), cập nhật [TEAM.md](../../TEAM.md) và [group_report.md](group_report.md).

## 4. Bằng chứng

- Nhánh `haivq`, commit `ffdcd4e` ("feat(p4): complete Person 4 E1 metrics, events, and launch dossier draft"), merge `ad5178f` vào `main`, và commit `90ed31d` ("docs(p4): fill A/B/E2 metrics in dossier and add Vu Quang Hai personal report").
- File: [src/cp5_chi_so.py](../../src/cp5_chi_so.py), [report/team/chi_so.md](chi_so.md) (E1 và 10 event), [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md), [TEAM.md](../../TEAM.md), [report/team/group_report.md](group_report.md).
- Lệnh `cd src && python cp5_chi_so.py` và `cd src && python lab13.py` chạy không lỗi, in đầy đủ các chỉ số E1 khớp số đối chiếu:

| Chỉ số (trong đợt chạy thử) | Toàn mẫu (1.200 yc) | Phạm vi pilot (982 yc) |
| --- | ---: | ---: |
| Chính (% đóng ≤ 24h, không mở lại 7 ngày) | 82,83% (994/1.200) | 92,26% (906/982) |
| Dùng (tỉ lệ bỏ qua gợi ý = `(sua + bo) / xem`) | 27,12% (48/177) | 21,09% (27/128) |
| An toàn (tỉ lệ lỗi lọt đến khách — mở lại 7 ngày) | 4,25% (51/1.200) | 3,97% (39/982) |

## 5. Công cụ AI đã dùng

- **Antigravity (Gemini):** đọc `PHAN_CONG.md` và đề bài, hỗ trợ viết module `src/cp5_chi_so.py`, soạn nháp phần E1/event trong `chi_so.md`, khung hồ sơ `ho_so_launch_v0.md`, `group_report.md` và báo cáo cá nhân này.
- **Cách tôi tự kiểm tra:**
  - Chạy trực tiếp `src/cp5_chi_so.py` và `src/lab13.py` trong `src/.venv`, đồng thời kiểm tra độc lập bằng thư viện chuẩn `csv` của Python — cả hai đều cho ra đúng `994/1200` (82,83%), `48/177` (27,12%), `51/1200` (4,25%).
  - Kiểm tra chéo từng chỉ số trong bảng E1 với danh sách 10 event để đảm bảo mọi chỉ số đều có event và `trace_id` đo được.
  - Kiểm tra quy tắc hồ sơ: mọi số tính từ cột `_simulated` đều có nhãn `simulated`, không ghi "cả đội" ở cột người phụ trách, không kết luận "trợ lý đã nâng chỉ số", và kiểm tra không vi phạm quy tắc 5 (chỉ duyệt kế hoạch pilot, không dùng từ cấm về chạy chính thức trong toàn bộ `report/team/`).

## 6. Tự đánh giá

- **Làm được:** hoàn thành đúng tiến độ và đúng ranh giới file của Người 4, giúp nhóm merge `haivq`, `p1-A`, `p2-B`, `p3-CD` vào `main` không xung đột; hồ sơ Gate 2a đủ 7 mục, nêu rõ cả con số bất lợi (B4 xem lại 100% lên 0,98×–1,03×; power 0,64 ở mức 5 điểm) và 4 điều kiện xử lý cụ thể.
- **Điều rút ra:**
  - Nếu một chỉ số không ánh xạ được về các event có `trace_id` thì chưa thể đo trong thực tế pilot; đồng thời cần khoá đơn nghiệp vụ chung (`order_id`) để bắt hoàn trùng khi phát sinh nhiều `request_id`.
  - Đợt chạy thử không có nhóm đối chứng nên chỉ được báo cáo "chỉ số trong đợt chạy thử là 82,83%", không được quy nhân quả cho trợ lý.
  - Phân loại lỗi phải bám nguyên nhân gốc (ví dụ lỗi ngầm như sai giá trong cache hay tốn token gấp 3 lần ở ca 12 không tạo ticket mở lại nên cần kiểm tra mẫu và giám sát chi phí định kỳ).
- **Cần hoàn thiện tiếp:** tham gia bảo vệ hồ sơ nhóm cùng Người 3 ở phiên duyệt chéo Gate 2a, sau đó điền kết quả duyệt chéo vào `report/team/group_report.md` và cập nhật commit chốt trong `TEAM.md` trước khi nộp LMS.
