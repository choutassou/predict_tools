# import sys
import date_span

# 開始日と終了日を設定
# start_date = sys.argv[1]  # datetime(2022, 1, 5)
# end_date = sys.argv[2]  # datetime(2023, 2, 28)
# ini_name = sys.argv[3]
# day_hour = sys.argv[4]
except_date = ["2023-01-01", "2022-12-31"]
# 営業日数を計算
# ds = date_span.count_days("2023-06-02 01:00", "2023-06-02 07:00", except_date)
# hs = date_span.count_hours("2023-06-02 01:00", "2023-06-02 07:00", except_date)
# print(f"d={ds},h={hs}")
# ds = date_span.count_days("2023-06-01 01:00", "2023-06-03 07:00", except_date)
# hs = date_span.count_hours("2023-06-01 01:00", "2023-06-03 07:00", except_date)
# print(f"d={ds},h={hs}")
ds = date_span.count_days("2022-12-29 01:00", "2023-01-03 07:00", except_date)
hs = date_span.count_hours("2022-12-29 01:00", "2023-01-03 07:00", except_date)
print(f"d={ds},h={hs}")
ds = date_span.count_days("2022-12-29 23:00", "2023-01-03 01:00", except_date)
hs = date_span.count_hours("2022-12-29 23:00", "2023-01-03 01:00", except_date)
print(f"d={ds},h={hs}")
# ds = date_span.count_days("2023-06-01 01:00", "2023-06-02 23:00", except_date)
# hs = date_span.count_hours("2023-06-01 01:00", "2023-06-02 23:00", except_date)
# print(f"d={ds},h={hs}")
