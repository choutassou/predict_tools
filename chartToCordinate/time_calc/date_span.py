import sys
import pandas as pd
from datetime import datetime, timedelta


def get_date_array(date_array):
    # 日付型の配列を作成します。
    date_array_datetime = []
    for date in date_array:
        date_array_datetime.append(datetime.strptime(date, "%Y-%m-%d").date())

    return date_array_datetime


# count days including start and end
def count_days(start_dt, end_dt, excepts):
    # 営業日カウンターを初期化
    business_days = 0

    start_dt = start_dt.replace(hour=0)  # 0時に丸める
    end_dt = end_dt.replace(hour=23)  # 23時に上丸める

    excepts_dt = get_date_array(excepts)

    # 日付範囲内の各日に対して処理を行う
    current_date = start_dt
    while current_date <= end_dt:
        # 土曜日や日曜日ならばスキップ
        if current_date.weekday() >= 5:
            current_date += timedelta(days=1)
            continue

        # 祝日ならばスキップ
        if current_date in excepts_dt:
            current_date += timedelta(days=1)
            continue

        # 営業日としてカウント
        business_days += 1
        current_date += timedelta(days=1)

    return business_days


# count hours including start and end
def count_hours(
    start_dt,
    end_dt,
    excepts,
):
    pasted = start_dt.hour
    remain = 24 - end_dt.hour
    days = count_days(start_dt, end_dt, excepts)

    if days == 1:
        all = 24
    else:
        all = int(23.5 * count_days(start_dt, end_dt, excepts))

    return all - pasted - remain
