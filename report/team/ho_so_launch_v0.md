# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi **Giả lập**. Người phụ trách là một vai trò cụ thể, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot.

Nhóm: LuckyTeam · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (`simulated`), gấp **16,3×** hoá đơn token+tool (274,7 đ/yc); giờ nhân viên chiếm 92,5% (làm lại 51,8%, xem lại 40,7%). Phạm vi `noi_dia` + `hang_nang` đã cộng cố định 40 triệu đ/tháng: **4.599 đ = 0,38×** ở 45.000 yc/tháng; **5.784 đ = 0,48×** ở 1/2 khối lượng (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. **Số ca làm lại ×2 (+51,8%**, lên 6.787 đ) · 2. **Tỉ lệ xem lại ×2 (+40,7%**, lên 6.292 đ) · 3. **Lương nhân viên +25% (+23,1%**, lên 5.506 đ). Đổi cặp token ×2 + xem lại ×2: +46,3% lên 6.543 đ (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống (gồm 222 ca NV làm thay): **5.865 đ/yc = 0,49×** của 12.000 đ; giới hạn **2 lần chạy** rẻ nhất cả hệ thống (**6.901.220 đ**). Phạm vi: `noi_dia` 0,22×, `hang_nang` 0,69×; loại `quoc_te` (1,88×) và `doi_tac` (0,85×). **Con số bất lợi (B4):** xem lại 100% lên **11.743 đ = 0,98×** (làm lại 9p) hoặc **12.415 đ = 1,03×** (làm lại 15,3p thực tế, `simulated`). | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (1.200 yc): Chính **82,83%** (994/1.200); Dùng — bỏ qua gợi ý **27,12%** (48/177); An toàn — mở lại 7 ngày **4,25%** (51/1.200). Phạm vi pilot (982 yc): 92,26% · 21,09% · 3,97%. Đủ 10 event có `trace_id` đo đủ 5 chỉ số. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập trùng **18/20 = 90%** (≥ 80%); ca 12 thống nhất **Ngầm**, ca 13 **Giới hạn hệ thống**. Bảng khắc phục **5 ca đủ 5 loại** (ca 9 · 7 · 18 · 4 · 17), mỗi ca có event + ngưỡng đo được và một vai trò phụ trách; ca 7 (sổ cái 503): ngưỡng **0 ca** báo "đã hoàn" khi ledger chưa thành công. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Scope `noi_dia` + `hang_nang`; chia ngẫu nhiên theo **staff 20 + 20** (20 cụm/nhóm, phân tầng depot). **MDE 6 điểm**, power 0,8: **859** hiệu dụng/nhóm (5.980 yc thô, DE 6,96). **Con số bất lợi:** nếu tác động thật chỉ 5 điểm, **power chỉ 0,64**. **4 luật dừng**: hoàn trùng ≥ 1 ca; mở lại 7 ngày > đối chứng +2 điểm hoặc > 6% (hiện 3,97%); CPS > 8.000 đ trong 2 tuần; bỏ qua gợi ý > 40% (hiện 21,09%). Rollout 10% → 25% → 50%, quyết định sớm nhất T+37. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | 3 rủi ro (bảng E2): (1) Làm lại ×2 → +51,8% lên **6.787 đ**; (2) Xem lại 100% kéo dài → **11.743–12.415 đ** (0,98×–1,03×); (3) Khối lượng còn 1/2 → cố định tăng từ +1.185 đ lên **+2.370 đ/việc** (tổng 5.784 đ) (`simulated`). | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho kế hoạch pilot phạm vi `noi_dia` và `hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85×), giới hạn tối đa **2 lần chạy**.

- **Điều kiện 1 (An toàn hệ thống):** Bổ sung khoá chống trùng lệnh hoàn tiền và cơ chế đối soát sổ cái hằng giờ (khắc phục lỗi ca 7 và ca 20) trước khi mở pilot. — *Người phụ trách:* Kỹ sư trưởng agent · *Ngày kiểm tra:* trước ngày bắt đầu pilot.
- **Điều kiện 2 (Thiết kế thống kê):** Giám đốc vận hành ký chấp nhận **MDE 6 điểm** cho phương án chia theo staff 20 + 20 (tối đa 1.000 < 1.251 hiệu dụng nên không đạt 5 điểm), biết rằng **power chỉ còn 0,64** nếu tác động thật là 5 điểm (`pilot_plan.yaml`). — *Người phụ trách:* Giám đốc vận hành LogiX-VN · *Ngày kiểm tra:* trước ngày bắt đầu pilot.
- **Điều kiện 3 (Đo lường thực tế):** Bật đủ 10 event có `trace_id` trong `chi_so.md` và thay hai cột phút `simulated` bằng thời gian xem lại, làm lại đo thật (`phut_xem_lai_thuc`, `phut_lam_lai_thuc`). — *Người phụ trách:* PM trợ lý hoàn phí · *Ngày kiểm tra:* cuối tuần 1 pilot.
- **Điều kiện 4 (Kiểm soát chi phí xem lại — xử lý rủi ro B4):** Có lộ trình hạ tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% và đưa thời gian xem lại ≤ 4,8 phút/ca (tránh mức 11.743–12.415 đ nếu giữ xem lại 100%). — *Người phụ trách:* Trưởng nhóm CSKH · *Ngày kiểm tra:* cuối bước rollout 0.25.
