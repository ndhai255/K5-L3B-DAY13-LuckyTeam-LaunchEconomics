# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): MeatProxy (L3B)
- Nhóm được chấm: LuckyTeam (L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** khớp bảng số: nêu rõ 2 con số bất lợi là B4 xem lại 100% lên **11.743–12.415 đ (0,98×–1,03×)** và power chỉ còn **0,64** nếu tác động thật 5 điểm; kèm 4 điều kiện có người phụ trách và ngày kiểm tra (lưu ý của hội đồng: khoá chống trùng lệnh hoàn tiền chưa chạy kiểm thử thực tế trước pilot). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ cột `_simulated` (4.472 đ, 5.865 đ, 6.901.220 đ, 11.743–12.415 đ, 4.599 đ, 5.784 đ) đều gắn nhãn `simulated`/`Giả lập`; phạm vi thu hẹp còn `noi_dia` (0,22×) + `hang_nang` (0,69×), loại `quoc_te` (1,88×, ok tụt 30,0% → 2,2%) và `doi_tac` (0,85×) (lưu ý của hội đồng: chi phí thực vẫn chờ đo lại sau tuần 1 pilot). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên theo **staff 20 + 20** (phân tầng depot); đủ cỡ mẫu MDE 6 điểm (**859** hiệu dụng/nhóm, **5.980** yc thô, DE 6,96); 4 luật dừng đủ NẾU–TRONG–THÌ–KHÔNG THÌ có ngưỡng số, thời hạn (T+37) và vai phụ trách cụ thể (lưu ý của hội đồng: cần theo dõi thêm rủi ro tràn tác động trong cùng depot). |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ đủ 7 mục, số liệu nhất quán, nêu thẳng các con số bất lợi (rủi ro xem lại 100% lên 1,03× của 12.000 đ và power 0,64 ở mức 5 điểm) cùng 4 điều kiện chặn trước/trong pilot (khoá chống trùng & đối soát sổ cái, ký chấp nhận MDE 6 điểm, bật đủ 10 event thay số `simulated`, lộ trình hạ xem lại ≤ 4,8 phút/ca).

**Một câu hỏi cho đội trình:** Nếu ở tuần 1–2 pilot, tỉ lệ sửa + bỏ của nhân viên vẫn > 15% nên chưa hạ được tỉ lệ xem lại 100%, nhóm làm thế nào để tránh chi phí thực tế vượt ngưỡng 12.000 đ/ca (1,03×)?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm áp dụng Điều kiện 4 và 2 luật dừng trong `pilot_plan.yaml`, cùng giới hạn tối đa 2 lần chạy (6.901.220 đ, rẻ nhất cả hệ thống) và mục tiêu xem lại ≤ 4,8 phút/ca (điểm hoà vốn B4). Nếu CPS đo thật vượt **8.000 đ** trong 2 tuần liên tiếp ở bước 0.50 thì PM trợ lý hoàn phí đóng băng scope và thu hẹp ca mới về `noi_dia`. Nếu tỉ lệ bỏ qua gợi ý > **40%** trong 1 tuần thì Trưởng nhóm CSKH phỏng vấn 5 nhân viên và rà 20 trace trong 3 ngày; chưa làm xong thì không được chuyển bước rollout.
