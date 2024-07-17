import os
import requests

# 選手番号入力処理
while True:
    try:
        bang = int(input("選手番号を入力: "))
        if bang == 0 or bang >= 5086:
            print("[Error]その番号は存在しません。")
        else:
            print("[Info]選手番号が選択されました。")
            break
    except ValueError:
        print("[Error]正しい整数を入力してください。")

# ディレクトリ作成処理
make_dir_path = 'C:\\Users\\takeh\\OneDrive\\デスクトップ\\vlhtml'
if os.path.isdir(make_dir_path):
    print("[Info]既にディレクトリが存在します。")
else:
    os.makedirs(make_dir_path)
    print("[Info]新しいディレクトリが作成されました。")

# HTMLダウンロード
url = f'https://vleague.jp/record/player_detail/{bang}'  # ダウンロードしたいページのURLを指定

file_name =str(input("ファイル名を指名してください。"))
if os.path.isdir('C:\\Users\\takeh\\OneDrive\\デスクトップ\\vlhtml\\'+file_name+'.txt'):
    print("[Error]すでにそのファイル名は存在します。")
else:
    print("[Info]適合検査完了")
    
file_title = 'C:\\Users\\takeh\\OneDrive\\デスクトップ\\vlhtml\\{file_name}'  # 保存するファイル名

response = requests.get(url)
with open(file_title, 'w', encoding='utf-8') as file:
    file.write(response.text)

print("[Info]HTMLファイルは"+file_title+"にダウンロードしました。")



