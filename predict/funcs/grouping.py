import random
import numpy as np


def mean_within_3sigma(array_a):
    """
    Args:
      array_a: 配列A

    Returns:
      3δ以内の値の算術平均値
    """
    # 平均値と標準偏差を計算
    mean = np.mean(array_a)
    std = np.std(array_a)
    # 3δ外の値を除外
    filtered_values = [x for x in array_a if abs(x - mean) <= 3 * std]
    # 3δ以内の値の算術平均を計算
    mean_filtered = np.mean(filtered_values)
    return mean_filtered


def grouping(xa, group_size):
    # xaとarrayYのサイズを取得
    data_size = len(xa)
    # to avoid override, there needs a minimum distance
    min_distance = group_size / 4
    # group number can be random get
    num_groups = data_size / group_size
    # print(f"num_groups={num_groups}, group_size={group_size}")

    # 抽出されたグループを格納するリスト
    groups = []

    while len(groups) < num_groups:
        # ランダムに起点を決定
        random_x = random.randint(0, data_size - group_size)
        find = False
        for xx in groups:
            if abs(xx - random_x) < min_distance:
                find = True
                break
        if not find:
            groups.append(random_x)

    # 結果を表示
    # print(groups)
    return groups


def get_deviation_grp(xa, ya, group_size, power):
    grps = grouping(xa, group_size)

    deviation_grp = 0
    for group_start_x in grps:
        xg = []
        yg = []

        # xg =[0,1,2...]
        for i in range(0, group_size - 2):
            xg.append(i)
            yg.append(ya[group_start_x + i])
        # get fitted coefficient
        coefficients = np.polyfit(xg, yg, power)

        # caculate fitted value
        y_fit = 0
        lastx = group_size - 1
        for coe in coefficients:
            y_fit = y_fit * lastx + coe

        # deviation of last vlaue in group
        deviation = abs(y_fit - yg[-1])
        deviation_grp = deviation_grp + deviation

    deviation_grp = deviation_grp / len(grps)
    return deviation_grp


def get_next_value(xa, ya, power):
    # get fitted coefficient

    coefficients = np.polyfit(xa, ya, power)

    # caculate fitted value
    y_fit = 0

    for coe in coefficients:
        y_fit = y_fit * (xa[-1] + 1) + coe

    return y_fit


"""
平均平方根誤差は、データ個数大きいほどに、値が大きくなる傾向
ですが、外れ値があった場合、より精確です

誤差絶対値平均は、データ個数に影響されることはないですが、外れ値の影響を受けやすいです

ここでは、誤差絶対値平均を採用します
データのグループサイズを変えて、最優を計算してるから。
"""
