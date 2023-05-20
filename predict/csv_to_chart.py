import funcs.grouping as groupx
import numpy as np
import argparse
import pandas as pd
import matplotlib.pyplot as plt

# a copy of predict
# This program has verified the effectiveness of the plot function.
#

# コマンドライン引数の定義
parser = argparse.ArgumentParser(description="Extract data points from a CSV file.")
parser.add_argument("csv_file", type=str, help="the input CSV file")

args = parser.parse_args()

# CSVファイルからデータを読み込み、x座標とy座標のリストを生成
df = pd.read_csv(args.csv_file, header=None)
x_data = df[0].tolist()
y_data = df[1].tolist()

grps = groupx.grouping(x_data, 298)

for grp in grps:
    xg = []
    yg = []
    for i in range(0, 297):
        xg.append(i)
        yg.append(y_data[grp + i])
    a, b, c, d, e = np.polyfit(xg, yg, 4)
    print(a, b)
# プロット
y_fit = [a * i * i * i * i + b * i * i * i + c * i * i + d * i + e for i in xg]

plt.plot(xg, yg, "r-", label="Data Points")
plt.plot(xg, y_fit, "b-", label="Least Squares Line")

plt.show()
