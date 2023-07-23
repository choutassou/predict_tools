import funcs.grouping as groupx
import argparse
import pandas as pd

# コマンドライン引数の定義
parser = argparse.ArgumentParser(description="Extract data points from a CSV file.")
parser.add_argument("csv_file", type=str, help="the input CSV file")

args = parser.parse_args()

# [group_size,power]の2次元配列
group_size_list = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
# group_size_list = [20, 25, 30, 35, 40]
power_list = [1, 2, 3]

# CSVファイルからデータを読み込み、x座標とy座標のリストを生成
df = pd.read_csv(args.csv_file, header=None)
x_data = df[0].tolist()
y_data = df[1].tolist()

min_abs_dv = 100000000
grp_size_memo = 20
power_memo = 2

# search best (m,p) for minimum deviation.
for grp_size in group_size_list:
    for power in power_list:
        # to 1 set of (m,p), get average of 10 times
        abs_dvs = []
        for i in range(3):
            abs_dvs.append(groupx.get_deviation_grp(x_data, y_data, grp_size, power))
        abs_dv = groupx.mean_within_3sigma(abs_dvs)
        print(f"abs_dv={abs_dv},{grp_size},{power}")

        # search minimum deviation in 27 kind of
        if min_abs_dv > abs_dv:
            grp_size_memo = grp_size
            power_memo = power
            min_abs_dv = abs_dv

#
print(f"m_b={grp_size_memo}, p_b={power_memo}")
#
# caculate next value
lx = range(grp_size_memo)
ly = y_data[-grp_size_memo:]

# :-D
next_y = groupx.get_next_value(lx, ly, power_memo)
delta = (next_y - ly[-1]) / ly[-1]
print(f"next_y={next_y}, delta={delta}")
