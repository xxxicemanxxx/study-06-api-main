import requests
import pandas as pd

REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
APP_ID = input("アプリIDを入力してください   ")
keyword = "ハリボー"

params = {
    'applicationId': APP_ID,
    'format':'json',
    'hits': 30,             #一度のリクエストで返してもらう最大個数（MAX30)
    'keyword':keyword,      #検索キーワード
    #'shopCode':shopName,
    'page':1,               #何ページ目か
    'postageFlag':1,        #送料込みの商品に限定
}

response = requests.get(REQUEST_URL , params)
result = response.json()
total = int(result['count'])
Max = total/30 + 1

#レスポンスが返ってきているかチェック 
# エラーはHTTPステータスコードで確認できる　200:OK 400:parameterエラー
print(response)
#print(response.status_code)     #こっちでもOK

print("【num of item】",total)
print("【num of page】",Max)
print("===================================")

counter = 0
price_list = []
for i in result['Items']:
    counter = counter + 1
    item = i['Item']
    name = item['itemName']
    print ("【No.】{}".format(str(counter)))
    print ("【Name】{}" .format(str(name)))
    print ("【Price】¥{}".format(str(item['itemPrice'])))
    price_list.append(int(item['itemPrice']))
    print ("【URL】{}".format(str(item['itemUrl'])))
    print ("【shop】{}".format(str(item['shopName'])))
    #print ("【text】{}".format(str(item['itemCaption'])))
    print ("\n")

print("最安値:{}".format(min(price_list)))
print("最高値:{}".format(max(price_list)))




