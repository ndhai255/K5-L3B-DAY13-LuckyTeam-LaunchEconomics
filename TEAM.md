# Team

## Thông tin nhóm

- Tên nhóm: LuckyTeam
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-LuckyTeam-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/ndhai255/K5-L3B-DAY13-LuckyTeam-LaunchEconomics` · nhánh `main` · commit chốt: commit cuối trên `main` trước deadline (code và hồ sơ chốt tại `6fa1222`; các commit sau chỉ cập nhật phiếu chấm, báo cáo nhóm và báo cáo cá nhân)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Đức Hải | 2A202603943 | ndhai255.work@gmail.com | ndhai255 | Người viết code (trước giải lao) — Nhiệm vụ A |
|   2 | Nguyễn Anh Quân | 2A202603950 | anhhquan511@gmail.com | anhhquan511 | Người kiểm số — Nhiệm vụ B & E2 |
|   3 | Tăng Nguyễn Hải Đăng | 2A202603916 | haidangg.work@gmail.com | haidangwork1411 | Người gắn nhãn 1, viết code sau giải lao — Nhiệm vụ C & D |
|   4 | Vũ Quang Hải | 2A202603935 | haivq25@gmail.com | HaiVuQ | Người gắn nhãn 2 kiêm giữ hồ sơ — Nhiệm vụ C (nhãn 2), E1, event & hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py` (Nhiệm vụ A, nối module cuối buổi).
- **Người kiểm số:** tính tay đối chiếu A1–A2, viết `src/cp2_do_nhay.py`, điền B1–B4 và rủi ro kinh tế E2.
- **Người gắn nhãn 1:** gắn nhãn 20 ca độc lập ở CP3, tổng hợp `report/team/bang_loi.md`, viết `src/cp4_co_mau.py` và `report/team/pilot_plan.yaml`.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** gắn nhãn 20 ca độc lập ở CP3, viết `src/cp5_chi_so.py`, điền E1 và danh sách event trong `report/team/chi_so.md`, dựng và cập nhật `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## NguyenDucHai-2A202603943

### Phần việc phụ trách

- Người viết code trước giải lao: nhiệm vụ A (CP1) trong `src/lab13.py` và phần A1–A4 của `report/team/bang_chi_phi.md`.
- Merge các nhánh `p1-A` → `p2-B` → `p3-CD` → `p4-E`, nối module vào `src/lab13.py` để chạy hết từ đầu đến cuối.
- Duyệt chéo Gate 2a cùng Người 2, chấm vào `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- A1: ba hàm kinh tế của việc chạy lại, qua ba phép thử 1,20 · 1,25 · 1,25.
- A2: `mo_hinh` (có nhánh `max_lan_chay`, trả thêm `chay_lai`, `hoa_don_moi_yc`); chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu.
- A3: tách theo 4 loại và tỉ lệ ok theo `attempt`; chỉ ra `quoc_te` không đáng xử lý (1,88× của 12.000 đ [simulated], tỉ lệ ok 30,0% → 11,4% → 2,2%).
- A4: cộng chi phí cố định 40 triệu đ/tháng cho `noi_dia` + `hang_nang`: 4.599 đ = 0,38× ở 45.000 yc/tháng, 5.784 đ = 0,48× ở một nửa khối lượng [simulated].

### Bằng chứng

- Nhánh `p1-A`, commit `5e91a4b` (A1–A4) và `1bd58d8` (báo cáo cá nhân).
- `cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và các bảng A2, A3, A4.
- Báo cáo cá nhân: [report/team/2A202603943_NguyenDucHai.md](report/team/2A202603943_NguyenDucHai.md).

## NguyenAnhQuan-2A202603950

### Phần việc phụ trách

- Người kiểm số (Người 2 trong `PHAN_CONG.md`): tính tay độc lập A1–A2 bằng pandas để đối chiếu với Người 1.
- CP2 · Nhiệm vụ B (B1–B4): viết module `src/cp2_do_nhay.py` (nhận `mo_hinh` làm tham số) và điền mục B1–B4 trong `report/team/bang_chi_phi.md`.
- CP5 · Nhiệm vụ E2: xây dựng bảng rủi ro kinh tế lấy số từ bảng độ nhạy trong `report/team/chi_so.md`.
- Duyệt chéo Gate 2a cùng Người 1, chấm hồ sơ nhóm bạn vào `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- Kiểm số độc lập A1 (`1,20 · 1,25 · 1,25`) và A2 (`4.373.585 đ`, `978` việc thành công, CPS `4.472 đ` [`simulated`], gấp `16,3×` hoá đơn/yêu cầu `274,7 đ`), đối chiếu khớp 100% với `lab13.mo_hinh`.
- B1–B2: chạy 9 kịch bản độ nhạy + kịch bản cặp `Token ×2 + Xem lại ×2` (`6.543 đ`, `+46,3%`, `simulated`), tự kiểm tra tuyến tính đạt; xếp hạng 3 yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (`+51,8%`) · 2. Tỉ lệ xem lại (`+40,7%`) · 3. Lương nhân viên (`+23,1%`).
- B3: so sánh chi phí cả hệ thống theo giới hạn chạy 1/2/3 lần, chỉ ra giới hạn 2 lần rẻ nhất cho công ty (`6.901.220 đ`, `simulated`) khác với mức CPS thấp nhất ở 1 lần (`4.111 đ`, đẩy thêm 85 ca sang nhân viên).
- B4 & E2: tính kịch bản xem lại 100% phạm vi `noi_dia` + `hang_nang` (`11.743 đ = 0,98×` với 9 phút làm lại và `12.415 đ = 1,03×` với trung bình thực tế 15,3 phút từ `phut_lam_lai_simulated`, mức hoà vốn `4,8–5,1 phút/ca`) và điền 3 dòng rủi ro kinh tế có vai phụ trách cụ thể vào `report/team/chi_so.md`.

### Bằng chứng

- Nhánh `p2-B`, commit `2599b35` (đã merge vào `main` tại `994a3ff` và nối vào `src/lab13.py` tại `3918943`).
- File: `src/cp2_do_nhay.py`, `report/team/bang_chi_phi.md` (mục B1–B4), `report/team/chi_so.md` (mục E2).
- `cd src && python cp2_do_nhay.py` đối chiếu khớp 100% với `lab13.mo_hinh` và qua toàn bộ kiểm tra tuyến tính B1–B2.
- Báo cáo cá nhân: [report/team/2A202603950_NguyenAnhQuan.md](report/team/2A202603950_NguyenAnhQuan.md).

## TangNguyenHaiDang-2A202603916

### Phần việc phụ trách

- Người gắn nhãn 1: gắn nhãn độc lập 20 ca CP3, đối chiếu với Người 4 và tổng hợp `report/team/bang_loi.md`.
- Phụ trách Nhiệm vụ D: `src/cp4_co_mau.py` và `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- CP3: hai bộ nhãn độc lập trùng 18/20 = 90%; nhãn thống nhất ca 12 là Ngầm, ca 13 là Giới hạn hệ thống; bảng khắc phục có 5 ca đủ 5 loại Google PAIR.
- CP4: D1 a=1.251; b=3.103 với DE=2,48; c=1.000; d=300; e=5.980 yêu cầu thô/nhánh, tương đương 859 mẫu hiệu dụng/nhánh với 20 staff, tối thiểu 299 yêu cầu/staff và DE=6,96.
- Pilot scope `noi_dia` + `hang_nang`; baseline mở lại toàn mẫu 51/1.200 = 4,25%, scope pilot 39/982 = 3,97%; rollout 10% → 25% → 50%, mốc quyết định đề xuất T+37.

### Bằng chứng

- File: `src/cp4_co_mau.py`, `report/team/pilot_plan.yaml`, `report/team/bang_loi.md`.
- `cd src && python cp4_co_mau.py` in đủ D1 và baseline; `yaml.safe_load` đọc được `pilot_plan.yaml`.
- Báo cáo cá nhân: [report/team/2A202603916_TangNguyenHaiDang.md](report/team/2A202603916_TangNguyenHaiDang.md).
- Nhánh `p3-CD`, commit `1fbd640` (đã merge vào `main` tại PR #2 `183a4ce` và tích hợp CP4 vào `src/lab13.py` tại `6fa1222`).

## VuQuangHai-2A202603935

### Phần việc phụ trách

- Người gắn nhãn 2 (gắn độc lập 20 ca lỗi CP3 để đối chiếu với Người 3).
- Nhiệm vụ E1 (tính thử 3 chỉ số, đề xuất 2 chỉ số mới) và đặc tả 10 event có `trace_id` kèm kiểm tra chéo.
- Giữ và cập nhật hồ sơ `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR dựa trên nguyên nhân gốc; so nhãn với Người 3 đạt đồng thuận **18/20 = 90%** (ca 12 thống nhất Ngầm, ca 13 thống nhất Giới hạn hệ thống).
- Viết module `src/cp5_chi_so.py` tính ba chỉ số E1 trên 1.200 yêu cầu (`82,83%`, `27,12%`, `4,25%`) và phạm vi pilot (`92,26%`, `21,09%`, `3,97%`).
- Hoàn thiện phần E1, bảng 10 event có `trace_id` và kiểm tra chéo trong `report/team/chi_so.md`.
- Dựng và cập nhật hồ sơ 7 mục trong `report/team/ho_so_launch_v0.md` (đủ số liệu A–E, đề xuất **Go có điều kiện** kèm 4 điều kiện có vai phụ trách và mốc kiểm tra), `TEAM.md` và `report/team/group_report.md`.

### Bằng chứng

- Nhánh `haivq`, commit `ffdcd4e` (phần việc Người 4), merge `ad5178f` vào `main`, và commit `90ed31d` (cập nhật số A/B/E2 vào hồ sơ & báo cáo cá nhân).
- File: `src/cp5_chi_so.py`, `report/team/chi_so.md` (E1 & 10 event), `report/team/ho_so_launch_v0.md`, `TEAM.md`, `report/team/group_report.md`.
- Báo cáo cá nhân: [report/team/2A202603935_VuQuangHai.md](report/team/2A202603935_VuQuangHai.md).
