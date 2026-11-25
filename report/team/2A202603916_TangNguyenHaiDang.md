# Báo cáo cá nhân — TangNguyenHaiDang-2A202603916

## 1. Thông tin thành viên

- Họ tên: Tăng Nguyễn Hải Đăng
- MSSV: 2A202603916
- Email: 26ai.dangtnh@vinuni.edu.vn
- GitHub: haidangwork1411
- Vai trong nhóm: Người gắn nhãn 1, viết code sau giải lao; phụ trách CP3 và CP4.

## 2. Phần việc phụ trách

- CP3: gắn nhãn độc lập 20 ca lỗi, đối chiếu với Người 4 và tổng hợp `report/team/bang_loi.md`.
- CP4: module `src/cp4_co_mau.py` và kế hoạch pilot `report/team/pilot_plan.yaml`.
- Phối hợp với Người 1 để tích hợp CP4 vào `src/lab13.py` và với Người 4 để cập nhật hồ sơ Gate 2a.

## 3. Đóng góp cụ thể

- Tự hoàn thành và chốt 20 nhãn gốc độc lập của Người 3 trước khi đối chiếu.
- Đối chiếu hai bộ nhãn: agreement 18/20 = 90%; bất đồng ở ca 12 và 13.
- Nhãn thống nhất ca 12 là Ngầm và ca 13 là Giới hạn hệ thống; hai bộ nhãn gốc vẫn được bảo toàn.
- Hoàn thiện module CP4 tính cỡ mẫu D1 và baseline mở lại trong 7 ngày.
- Hoàn thiện `pilot_plan.yaml`: random theo staff 20+20, MDE 6 điểm, 5.980 yêu cầu thô/nhánh tương đương 859 mẫu hiệu dụng/nhánh, rollback và ba stop rule.

## 4. Bằng chứng

- `src/cp4_co_mau.py`: D1 a=1.251; b=3.103, DE=2,48; c=1.000; d=300; e=859 hiệu dụng, m=299, DE=6,96.
- Baseline an toàn: 51/1.200 = 4,25%; scope `noi_dia` + `hang_nang`: 39/982 = 3,97%.
- `report/team/pilot_plan.yaml` qua `yaml.safe_load`, không placeholder và có ba stop rule đủ NẾU–TRONG–THÌ–KHÔNG THÌ.
- Hai bộ nhãn CP3: 18/20 trùng, 90%; hai ca bất đồng là 12 và 13.
- Các file CP3/CP4 chưa được commit tại thời điểm báo cáo này.

## 5. Công cụ AI đã dùng

- Codex: hỗ trợ viết và rà soát module CP4, kiểm tra công thức/cỡ mẫu, chạy kiểm thử, kiểm tra YAML, đối chiếu tài liệu và soạn nháp báo cáo.
- Codex đã chạy `cp4_co_mau.py`, `lab13.py`, kiểm tra baseline từ CSV, `yaml.safe_load`, placeholder và `git diff --check` trong workspace.


## 6. Tự đánh giá

- Đã hoàn tất phần tính cỡ mẫu, baseline an toàn, pilot plan và đối chiếu agreement CP3.
- Cần Người 1 tích hợp CP4 vào `lab13.py`, Người 4 cập nhật Mục 5–6 hồ sơ launch và cập nhật thông tin Người 3 trong `TEAM.md`.
