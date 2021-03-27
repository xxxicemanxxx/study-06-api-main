import requests
import pandas as pd
import datetime

REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
APP_ID = input("アプリIDを入力してください   ")

params = {
    'applicationId': APP_ID,
    'format':'json',
    'formatVersion': 2,
    #'genreId': 0,
    #'genreId': '568376',   #PlayStation 5
    'genreId': '100324',    #ビール・発泡酒
    #'genreId': '100227',    #食品
}

response = requests.get(REQUEST_URL , params)
result = response.json()
df_genre = pd.DataFrame()
now = datetime.datetime.now()
failname = now.strftime('%Y%m%d_%H%M%S') 

#レスポンスが返ってきているかチェック 
# エラーはHTTPステータスコードで確認できる　200:OK 400:parameterエラー
print(response)
#print(response.status_code)     #こっちでもOK

def file_write(str):
    #with openにすれば自動でファイルが閉じる　　引数　、mode='w'書き込み用、encoding = utf-8-sig：デフォルト状態
    #mode='a'追記
    with open("genreList_log_{}.txt".format(failname),mode='a',encoding = "utf-8-sig") as log_file:
        log_file.write(str+"\n")
        print(str)

itemName_list = []
itemPrice_list = []
genre_id_list = []
rank_list = []

for i in result['Items']:
    itemName_list.append(i["itemName"])
    itemPrice_list.append(i["itemPrice"])
    genre_id_list.append(i["genreId"])
    rank_list.append(i["rank"])
    file_write("{},{},{},{}".format(i["rank"],i["itemName"],i["itemPrice"],i["genreId"]))


    # 最上段ジャンルに紐づく、子ジャンル情報の取得
    genre_list = []
    df_genre = pd.DataFrame({'商品名':itemName_list,'商品価格':itemPrice_list,'ジャンルID':genre_id_list})
    df_genre.to_csv("genreList_{}.csv".format(failname), encoding = "utf-8-sig")
