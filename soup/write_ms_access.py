import pyodbc
from datetime import datetime


def write_to_msacc(tbl_name, bid, sel):
    # Accessデータベースファイルへのパス
    database_file_path = r"C:\DATA\fx.accdb"

    # ODBCドライバーとデータベースファイルの指定
    connection_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + database_file_path
    )

    # データベースに接続
    conn = pyodbc.connect(connection_str)

    # カーソルを作成
    cursor = conn.cursor()

    current_time = datetime.now()
    data_to_insert = (current_time, bid, sel)

    # データをテーブルに挿入するSQLクエリを実行
    insert_query = f"INSERT INTO {tbl_name} (date1, bid, sel) VALUES (?, ?, ?)"
    cursor.execute(insert_query, data_to_insert)

    # 変更をデータベースにコミット
    conn.commit()

    # 接続を閉じる
    cursor.close()
    conn.close()
