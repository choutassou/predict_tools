# This module can get data from a chart graph

import sys
import csv
from PIL import Image


# judge data point (red)
def is_red(px):
    fr = float(px[0])
    fg = float(px[1])
    fb = float(px[2])
    return fr / (fg + 1) > 2.0 and fr / (fb + 1) > 2.0


# pixel cordinate to data value
def getY(h, py, u):
    return float(h - 1 - py) / u


# data value to pixel cordinate
def getPY(h, y, u):
    return h - 1 - int(y * u)


# main
image_file = sys.argv[1]
x_start = int(sys.argv[2])  # int, hours from xxx
y_start = float(sys.argv[3])  # float, under bound of value
width = int(sys.argv[4])  # int, hours in the chart
height = float(sys.argv[5])  # float, top bound of value

img = Image.open(image_file)
img_width, img_height = img.size

# 軸の単位長を計算、Xは整数、YはFloat
x_unit = img_width / width
y_unit = float(img_height) / height
print(f"pixel number per unit x={x_unit} y={y_unit}")

# データポイントを記録するリストを初期化
data_points = []
last_y = 0.0
x = 0
y = None

# 一番左のy値を取得
for py in range(img_height - 1, 0, -1):
    px_info = img.getpixel((0, py))
    if is_red(px_info):
        y = getY(img_height, py, y_unit)
        data_points.append((x_start, y + y_start))
        break
if y is None:
    print("error: left edge of the image must has a data. (red point)")
    exit()

x = 1
# x軸方向にループ
while True:
    step = 0
    px = x * x_unit
    if px >= img_width:
        break
    # y軸方向にループの起点
    py = getPY(img_height, y, y_unit)
    py_up = py
    py_down = py
    # y軸方向にループ
    while True:
        if py_up < img_height:
            px_info = img.getpixel((px, py_up))
            if is_red(px_info):
                y = getY(img_height, py_up, y_unit)
                break
            py_up = py_up + 1
        if py_down >= 0:
            px_info = img.getpixel((px, py_down))
            if is_red(px_info):
                y = getY(img_height, py_down, y_unit)
                break
            py_down = py_down - 1
        if py_up >= img_height and py_down < 0:
            break
    data_points.append((x + x_start, y + y_start))
    x = x + 1

csv_file_path = image_file.replace("png", "csv")

with open(csv_file_path, "w", newline="\n") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["x", "y"])
    for x, y in data_points:
        csv_writer.writerow([x, y])
