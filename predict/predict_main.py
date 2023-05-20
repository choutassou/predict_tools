import funcs.grouping as groupx
import argparse
import pandas as pd

# コマンドライン引数の定義
parser = argparse.ArgumentParser(description="Extract data points from a CSV file.")
parser.add_argument("csv_file", type=str, help="the input CSV file")

args = parser.parse_args()

# [group_size,power]の2次元配列
size_list = [20, 25, 30, 35, 40, 55, 60]
power_list = [1, 2, 3]

# CSVファイルからデータを読み込み、x座標とy座標のリストを生成
df = pd.read_csv(args.csv_file, header=None)
x_data = df[0].tolist()
y_data = df[1].tolist()

min_abs_dv = 100000000
m_b = 20
p_b = 2

# search best m and p
for m in size_list:
    for p in power_list:
        abs_dv = groupx.get_deviation_grp(x_data, y_data, m, p)
        if min_abs_dv > abs_dv:
            m_b = m
            p_b = p
            min_abs_dv = abs_dv

print(f"m_b={m_b}, p_b={p_b}")
#
# caculate next value
lx = range(m_b)
ly = y_data[-m_b:]

# :-D
next_y = groupx.get_next_value(lx, ly, p_b)
# print(ly)
print(f"next_y={next_y}")
