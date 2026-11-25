"""CP4/D — cỡ mẫu và baseline an toàn cho Lab 13.

Module này chạy độc lập và không thực hiện I/O khi được import.  Người 1 có
thể import ``d1_ket_qua`` và ``ty_le_mo_lai`` vào ``lab13.py`` ở bước tích
hợp cuối cùng.
"""

from __future__ import annotations

import math
from pathlib import Path
from statistics import NormalDist
from typing import Any

import pandas as pd


BASELINE = 0.70
ALPHA = 0.05
POWER = 0.80
ICC = 0.02
MDE_NAM_DIEM = 0.05
MDE_SAU_DIEM = 0.06
NHAN_VIEN_MOI_CUM = 75
NHAN_VIEN_MOI_NHANH = 20
DEPOT_MOI_NHANH = 6


def co_mau_moi_nhanh(
    p1: float,
    p2: float,
    alpha: float = ALPHA,
    power: float = POWER,
) -> int:
    """Trả về cỡ mẫu mỗi nhánh khi so sánh hai tỷ lệ độc lập.

    Dùng đúng công thức CP4/D1 với z chính xác từ ``NormalDist`` và làm tròn
    lên để không thiếu power.
    """
    if not (0 < p1 < 1 and 0 < p2 < 1 and p1 != p2):
        raise ValueError("p1 và p2 phải thuộc (0, 1) và khác nhau")
    if not (0 < alpha < 1 and 0 < power < 1):
        raise ValueError("alpha và power phải thuộc (0, 1)")

    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_power = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    numerator = (
        z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
        + z_power * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    ) ** 2
    return math.ceil(numerator / (p2 - p1) ** 2)


def he_so_thiet_ke(cum_size: int, icc: float = ICC) -> float:
    """Trả về DE = 1 + (m - 1) * ICC."""
    if cum_size < 1 or not 0 <= icc < 1:
        raise ValueError("cum_size phải >= 1 và ICC phải thuộc [0, 1)")
    return 1 + (cum_size - 1) * icc


def co_mau_hieu_dung(so_cum: int, cum_size: int, icc: float = ICC) -> float:
    """Trả về cỡ mẫu hiệu dụng của thiết kế chia cụm."""
    if so_cum < 1:
        raise ValueError("so_cum phải >= 1")
    return so_cum * cum_size / he_so_thiet_ke(cum_size, icc)


def gioi_han_hieu_dung(so_cum: int, icc: float = ICC) -> float:
    """Trả về giới hạn trên c / ICC của cỡ mẫu hiệu dụng."""
    if so_cum < 1 or not 0 < icc < 1:
        raise ValueError("so_cum phải >= 1 và ICC phải thuộc (0, 1)")
    return so_cum / icc


def so_cum_toi_thieu(
    co_mau_muc_tieu: int, cum_size: int, icc: float = ICC
) -> int:
    """Số cụm tối thiểu mỗi nhánh để đạt cỡ mẫu mục tiêu."""
    if co_mau_muc_tieu < 1:
        raise ValueError("co_mau_muc_tieu phải >= 1")
    return math.ceil(
        co_mau_muc_tieu * he_so_thiet_ke(cum_size, icc) / cum_size
    )


def cum_size_toi_thieu(
    co_mau_muc_tieu: int, so_cum: int, icc: float = ICC
) -> int:
    """Tìm m nhỏ nhất để c*m/(1+(m-1)*ICC) đạt cỡ mẫu mục tiêu.

    Không có nghiệm hữu hạn nếu mục tiêu lớn hơn hoặc bằng c / ICC.
    """
    if co_mau_muc_tieu < 1 or so_cum < 1 or not 0 < icc < 1:
        raise ValueError("tham số không hợp lệ")
    denominator = so_cum - co_mau_muc_tieu * icc
    if denominator <= 0:
        raise ValueError("mục tiêu không thể đạt với số cụm và ICC này")
    return math.ceil(co_mau_muc_tieu * (1 - icc) / denominator)


def d1_ket_qua() -> dict[str, Any]:
    """Tính toàn bộ năm câu D1 từ các tham số chính thức của đề bài."""
    n_5_diem = co_mau_moi_nhanh(BASELINE, BASELINE + MDE_NAM_DIEM)
    de_75 = he_so_thiet_ke(NHAN_VIEN_MOI_CUM)
    n_nhan_vien_75 = math.ceil(n_5_diem * de_75)
    n_nv_moi_nhanh = so_cum_toi_thieu(n_5_diem, NHAN_VIEN_MOI_CUM)
    n_6_diem = co_mau_moi_nhanh(BASELINE, BASELINE + MDE_SAU_DIEM)
    m_cho_6_diem = cum_size_toi_thieu(
        n_6_diem, NHAN_VIEN_MOI_NHANH
    )
    de_cho_6_diem = he_so_thiet_ke(m_cho_6_diem)

    return {
        "a_request_randomization_n_per_arm": n_5_diem,
        "b_staff_m": NHAN_VIEN_MOI_CUM,
        "b_design_effect": de_75,
        "b_n_per_arm": n_nhan_vien_75,
        "b_staff_per_arm": n_nv_moi_nhanh,
        "c_staff_per_arm": NHAN_VIEN_MOI_NHANH,
        "c_effective_n_upper_bound": gioi_han_hieu_dung(NHAN_VIEN_MOI_NHANH),
        "d_depot_per_arm": DEPOT_MOI_NHANH,
        "d_effective_n_upper_bound": gioi_han_hieu_dung(DEPOT_MOI_NHANH),
        "e_mde": MDE_SAU_DIEM,
        "e_n_per_arm": n_6_diem,
        "e_staff_per_arm": NHAN_VIEN_MOI_NHANH,
        "e_min_requests_per_staff": m_cho_6_diem,
        "e_design_effect": de_cho_6_diem,
        "e_effective_n": co_mau_hieu_dung(
            NHAN_VIEN_MOI_NHANH, m_cho_6_diem
        ),
    }


def ty_le_mo_lai(
    duong_dan: str | Path,
    loai_pilot: tuple[str, ...] | None = None,
) -> dict[str, Any]:
    """Tính tỷ lệ ``mo_lai_trong_7_ngay`` cùng tử số, mẫu số và bộ lọc.

    ``loai_pilot=None`` trả về toàn bộ mẫu.  Đọc CSV với
    ``keep_default_na=False`` theo yêu cầu của lab.
    """
    reqs = pd.read_csv(duong_dan, keep_default_na=False)
    required = {"loai", "mo_lai_trong_7_ngay"}
    missing = required.difference(reqs.columns)
    if missing:
        raise ValueError(f"CSV thiếu cột: {', '.join(sorted(missing))}")

    if loai_pilot is not None:
        reqs = reqs[reqs["loai"].isin(loai_pilot)]
    if reqs.empty:
        raise ValueError("bộ lọc không có yêu cầu nào")

    values = pd.to_numeric(reqs["mo_lai_trong_7_ngay"], errors="raise")
    invalid = set(values.unique()).difference({0, 1})
    if invalid:
        raise ValueError(f"giá trị mo_lai_trong_7_ngay không hợp lệ: {invalid}")
    numerator = int((values == 1).sum())
    denominator = int(len(values))
    return {
        "numerator": numerator,
        "denominator": denominator,
        "rate": numerator / denominator,
        "scope": "toàn bộ dữ liệu" if loai_pilot is None else list(loai_pilot),
    }


def in_bao_cao_d1(ket_qua: dict[str, Any] | None = None) -> None:
    """In kết quả D1 dễ chép vào chú thích pilot_plan.yaml."""
    r = d1_ket_qua() if ket_qua is None else ket_qua
    print("D1 · Cỡ mẫu")
    print(f"a) Chia theo yêu cầu: {r['a_request_randomization_n_per_arm']} mỗi nhóm")
    print(
        "b) Theo nhân viên, m=75: "
        f"DE={r['b_design_effect']:.2f}; {r['b_n_per_arm']} mỗi nhóm; "
        f"{r['b_staff_per_arm']} nhân viên mỗi nhóm"
    )
    print(
        "c) 20 nhân viên mỗi nhóm: "
        f"tối đa {r['c_effective_n_upper_bound']:.0f} hiệu dụng"
    )
    print(
        "d) 6 depot mỗi nhóm: "
        f"tối đa {r['d_effective_n_upper_bound']:.0f} hiệu dụng"
    )
    print(
        "e) MDE 6 điểm, 20 nhân viên mỗi nhóm: "
        f"{r['e_n_per_arm']} mỗi nhóm; ít nhất "
        f"{r['e_min_requests_per_staff']} yêu cầu/nhân viên; "
        f"DE={r['e_design_effect']:.2f}; "
        f"n hiệu dụng={r['e_effective_n']:.0f}"
    )


def main() -> None:
    """Chạy CP4 độc lập từ thư mục src/ hoặc từ đường dẫn bất kỳ."""
    in_bao_cao_d1()
    csv_path = Path(__file__).with_name("logix_requests.csv")
    all_data = ty_le_mo_lai(csv_path)
    pilot_scope = ty_le_mo_lai(csv_path, ("noi_dia", "hang_nang"))
    print("\nBaseline mở lại trong 7 ngày")
    print(
        f"- Toàn bộ dữ liệu: {all_data['numerator']}/{all_data['denominator']} "
        f"= {all_data['rate']:.2%}"
    )
    print(
        "- Phạm vi noi_dia + hang_nang: "
        f"{pilot_scope['numerator']}/{pilot_scope['denominator']} "
        f"= {pilot_scope['rate']:.2%}"
    )


if __name__ == "__main__":
    main()
