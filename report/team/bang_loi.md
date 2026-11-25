# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Tăng Nguyễn Hải Đăng · Người gắn nhãn 2: Vũ Quang Hải. Hai bộ nhãn dưới đây là nhãn gốc độc lập và không được sửa để nâng agreement.

| Ca | Nhãn Người 3 | Nhãn Người 4 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Hệ thống | Ngầm | Không | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = **90%**, đạt ngưỡng 80% (16/20). Đây là agreement giữa hai người gắn nhãn, không phải độ chính xác so với đáp án giảng viên.

## Quy tắc phân biệt cho các ca không trùng

Hai nhãn thống nhất dưới đây không sửa hai bộ nhãn gốc.

- **Ca 12 — Hệ thống và Ngầm:** dùng **Ngầm** khi kết quả hoặc chi phí sai lệch kéo dài nhưng cả khách, nhân viên và hệ thống không phát hiện; dùng Hệ thống khi hành vi sai so với thiết kế hoặc chính sách đã lộ ra.
- **Ca 13 — Hệ thống và Giới hạn hệ thống:** dùng **Giới hạn hệ thống** khi yêu cầu nằm ngoài phạm vi, dữ liệu hoặc khả năng xử lý; chỉ dùng Hệ thống khi chức năng vốn nằm trong phạm vi nhưng trợ lý vi phạm thiết kế hoặc chính sách.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". Các event đều có trong `chi_so.md`; giá trị chuẩn hoá của trường `reason` là đề xuất triển khai, không phải event mới. Ngưỡng của ca 4 và ca 18 là ngưỡng đề xuất, không phải số liệu thực nghiệm.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | `handoff_to_staff` có `reason=ma_khong_hop_le`; cảnh báo khi vượt 2% yêu cầu/ngày | Nhận diện mã sàn, gợi ý chuyển sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh hoặc chuyển nhân viên | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ `refund_ledger_write` có `ket_qua` khác thành công; ngưỡng 0 ca được xác nhận hoàn tiền trước khi ledger thành công | Chỉ thông báo hoàn tiền sau khi ledger thành công; lỗi 503 sau 3 lần thì báo đang xử lý và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | `ticket_reopened` có `reason=so_tien_hoac_cach_tinh`; cảnh báo khi vượt **1% số yêu cầu đã đóng trong scope/tuần** (ngưỡng đề xuất) | Tin nhắn luôn nêu công thức, ví dụ `30.000 đ × 50% = 15.000 đ` | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | `handoff_to_staff` có `reason=thieu_du_lieu`; cảnh báo khi vượt **2% yêu cầu trong scope/tuần** (ngưỡng đề xuất) | Chuyển nhân viên kèm tóm tắt; giữ `quoc_te` ngoài scope pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked`: kiểm tra 100 đơn/tuần so với bảng giá hiện hành; cảnh báo khi trên 1% đơn lệch | Xóa cache khi bảng giá đổi, lưu version bảng giá vào trace | Kế toán trưởng |
