import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import schedule
import time
import write_ms_access


def connect_sbi(ACCOUNT="", PASSWORD="", name=""):
    options = Options()
    # ヘッドレスモード(chromeを表示させないモード)
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, executable_path="get_sbi/chromedriver")

    # SBI証券のトップ画面を開く
    driver.get("https://site0.sbisec.co.jp/marble/exchange/top.do?")

    return driver


def fx_soup(driver):
    # 遷移するまで待つ
    time.sleep(4)

    # 文字コードをUTF-8に変換
    html = driver.page_source.encode("utf-8")

    # BeautifulSoupでパース
    soup = BeautifulSoup(html, "html.parser")

    datas = []
    tbl_names = {
        "米ドル/円": "dolla_en",
        "ユーロ/円": "euro_en",
        "英ポンド/円": "pound_en",
        "豪ドル/円": "aud_en",
        "NZドル/円": "nzd_en",
        "カナダドル/円": "cad_en",
        "南アランド/円": "rnd_en",
        "メキシコペソ/円": "mps_en",
        "人民元/円": "rmb_en",
        "トルコリラ/円": "try_en",
    }
    # 株式
    table_data = soup.find("table", attrs={"class": "md-t-table04"})
    for tr in table_data.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) > 2:
            datas.append([tds[0].text, tds[1].text])
    datas_t = [[item[0], item[1].replace("\xa0-\xa0", ",")] for item in datas]
    datas = [
        [tbl_names.get(item[0]), item[1].split(",")[0], item[1].split(",")[1]]
        for item in datas_t
    ]
    for item in datas:
        write_ms_access.write_to_msacc(item[0], float(item[1]), float(item[2]))


def job():
    now = datetime.datetime.now()
    weekday = now.weekday()
    hour = now.hour

    # 土曜日6:00 AM～月曜日 6:00 AMの間は、動かさない
    if weekday == 5 and hour >= 6:  # 土曜日の6:00以降
        return
    elif weekday == 6:  # 日曜日
        return
    elif weekday == 0 and hour < 6:  # 月曜日の6:00未満
        return

    # 毎日の朝6:00のみ動かせたくない
    if hour == 6:
        return

    fx_soup(connect_sbi())


# 毎時0分に実行するようにスケジューリング
schedule.every().hour.at(":00").do(job)

for i in range(0, 14):
    if datetime.datetime.now().minute == 0:
        job()
        exit()
    time.sleep(60)
