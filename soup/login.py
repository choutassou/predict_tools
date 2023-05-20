import os
import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def connect_sbi(ACCOUNT, PASSWORD, name):
    options = Options()
    # ヘッドレスモード(chromeを表示させないモード)
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, executable_path="get_sbi/chromedriver")

    # SBI証券のトップ画面を開く
    driver.get("https://www.sbisec.co.jp/ETGate")

    # ユーザーIDとパスワード
    input_user_id = driver.find_element_by_name("user_id")
    input_user_id.send_keys("cyoudatu")
    input_user_password = driver.find_element_by_name("user_password")
    input_user_password.send_keys("_Yy135797531")

    # ログインボタンをクリック
    driver.find_element_by_name("ACT_login").click()

    return driver


def get_ja_data(driver):
    # 遷移するまで待つ
    time.sleep(4)

    # ポートフォリオの画面に遷移
    driver.find_element_by_xpath('//*[@id="link02M"]/ul/li[1]/a/img').click()

    # 文字コードをUTF-8に変換
    html = driver.page_source.encode("utf-8")

    # BeautifulSoupでパース
    soup = BeautifulSoup(html, "html.parser")

    # 株式
    table_data = soup.find_all(
        "table", bgcolor="#9fbf99", cellpadding="4", cellspacing="1", width="100%"
    )

    # 株式（現物/特定預り）
    df_stock_specific = pd.read_html(str(table_data), header=0)[0]
    df_stock_specific = format_data(df_stock_specific, "株式（現物/特定預り）", "上場ＴＰＸ")

    # 結合
    df_ja_result = pd.concat(
        [
            df_stock_specific,
            df_stock_fund_nisa,
            df_fund_specific,
            df_fund_nisa,
            df_fund_nisa_tsumitate,
        ]
    )
    df_ja_result["date"] = datetime.date.today()

    return df_ja_result
