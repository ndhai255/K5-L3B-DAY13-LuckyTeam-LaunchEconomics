"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i=1..k
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # = E[số lần chạy] / P(thành công) = 1/p với mọi k (k triệt tiêu)
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    Trả thêm: chay_lai (token + tool của lần chạy attempt > 1), hoa_don_moi_yc ((token + tool) / số yêu cầu).
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # B1, B3: bỏ lần chạy vượt giới hạn, yêu cầu vượt coi là chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    # Tử số: MỌI lần chạy, kể cả lần lỗi
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
LOAI = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']


def tach_theo_loai(runs, reqs):
    """A3: gọi lại mo_hinh cho từng loại; trả DataFrame một dòng mỗi loại."""
    dong = []
    for loai in LOAI:
        con = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, con)
        dong.append(dict(loai=loai, so_yc=len(con), ti_le_tc=r['thanh_cong'] / len(con),
                         lan_chay_moi_yc=con['so_lan_chay'].mean(), cps=r['cps'],
                         so_voi_baseline=r['cps'] / BASELINE))
    return pd.DataFrame(dong).set_index('loai')


def ti_le_ok_theo_lan_chay(runs, reqs):
    """A3: tỉ lệ status == 'ok' theo loai × attempt (chạy lại có giúp không)."""
    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    m['ok'] = (m['status'] == 'ok').astype(float)
    return m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').reindex(LOAI)


# ---------- Nhiệm vụ A4 · Chi phí cố định ----------
CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
KHOI_LUONG_THANG = 45_000      # yêu cầu / tháng của toàn công ty
PHAM_VI_PILOT = ['noi_dia', 'hang_nang']


def chi_phi_co_dinh(runs, reqs, khoi_luong=KHOI_LUONG_THANG, pham_vi=PHAM_VI_PILOT):
    """A4: cộng chi phí cố định vào chi phí mỗi việc thành công trong phạm vi pilot.
    Việc thành công mỗi tháng = khối lượng × (thành công trong phạm vi / 1.200 yêu cầu của mẫu),
    vì 45.000 là khối lượng của cả công ty (mọi loại)."""
    r = mo_hinh(runs, reqs[reqs['loai'].isin(pham_vi)])
    tc_thang = khoi_luong * r['thanh_cong'] / len(reqs)
    co_dinh = CHI_PHI_CO_DINH / tc_thang
    tong = r['cps'] + co_dinh
    return dict(khoi_luong=khoi_luong, tc_thang=tc_thang, co_dinh_moi_viec=co_dinh,
                cps_pham_vi=r['cps'], cps_cong_co_dinh=tong, so_voi_baseline=tong / BASELINE)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated)')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    print(f"cps / hoa_don_moi_yc = {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua['tong']:6.1%}")

    # Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\nA3 · Theo loại (cps: simulated)')
    print(tach_theo_loai(runs, reqs).round(3).to_string())
    print('\nA3 · Tỉ lệ ok theo lần chạy (attempt)')
    print(ti_le_ok_theo_lan_chay(runs, reqs).round(3).to_string())

    # Nhiệm vụ A4: chi phí cố định, phạm vi noi_dia + hang_nang.
    print('\nA4 · Chi phí cố định 40 triệu/tháng (noi_dia + hang_nang, simulated)')
    for kl in [KHOI_LUONG_THANG, KHOI_LUONG_THANG // 2]:
        a4 = chi_phi_co_dinh(runs, reqs, khoi_luong=kl)
        print(f"{kl:>7,d} yc/tháng: {a4['tc_thang']:>8,.0f} việc TC, cố định {a4['co_dinh_moi_viec']:>6,.0f} đ/việc, "
              f"{a4['cps_pham_vi']:,.0f} + cố định = {a4['cps_cong_co_dinh']:,.0f} đ = {a4['so_voi_baseline']:.2f}×")

    # Nhiệm vụ B (Người 2): kiểm số độc lập A1–A2, độ nhạy B1–B4, số liệu E2.
    from cp2_do_nhay import kiem_tra_a1_a2_doc_lap, chay_do_nhay
    print()
    kiem_tra_a1_a2_doc_lap(runs, reqs, mo_hinh=mo_hinh)
    chay_do_nhay(mo_hinh, runs, reqs)

    # Nhiệm vụ D (Người 3): cỡ mẫu D1 và tỉ lệ mở lại hiện tại trước khi đặt luật an toàn.
    from cp4_co_mau import d1_ket_qua, in_bao_cao_d1, ty_le_mo_lai
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    print('\n=== Nhiệm vụ D · Cỡ mẫu pilot ===')
    d1 = d1_ket_qua()
    in_bao_cao_d1(d1)
    # Con số bất lợi của đánh đổi MDE 6 điểm: power nếu tác động thật chỉ là 5 điểm.
    power_5_diem = NormalIndPower().power(proportion_effectsize(0.75, 0.70),
                                          nobs1=d1['e_n_per_arm'], alpha=0.05)
    print(f"Power nếu tác động thật chỉ 5 điểm (n hiệu dụng={d1['e_n_per_arm']}/nhóm): {power_5_diem:.2f}")
    print('Tỉ lệ mo_lai_trong_7_ngay hiện tại:')
    for ten, loai in [('Toàn bộ mẫu', None), ('noi_dia + hang_nang', tuple(PHAM_VI_PILOT))]:
        r = ty_le_mo_lai('logix_requests.csv', loai)
        print(f"  {ten:20s} {r['numerator']}/{r['denominator']} = {r['rate']:.2%}")

    # Nhiệm vụ E1 (Người 4): ba chỉ số chính, dùng, an toàn.
    from cp5_chi_so import chay_chi_so
    print()
    chay_chi_so(reqs)
