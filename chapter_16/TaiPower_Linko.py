"""
行政院環境保護署。環境資源資料開放平臺
https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-001175?sort=M_Time&offset=0&limit=1000
*---------------------------*
|方法一：透過「應用程式存取網址」|
*---------------------------*
1.格式：
https://opendata.epa.gov.tw/webapi/api/rest/datastore/{resourceID}/?format={format}&limit={limit}&offset={offset}&sort={sort}&token={token}

2.參數
{resourceID}    資料代號，各資料頁面內透過連結可取得[例："355000000I-000208"]。
{format}        資料格式，可選擇 json、xml、csv[例："json"]。
{limit}         取最前n筆資料，請填入數字，最大值為1000[例："1000"]。
{offset}        跳過筆數，請填入數字[例："0"]。
{sort}          排序之欄位名稱[例："SiteId"]。
{token}         資料下載驗證碼，「會員註冊」頁面進行登記後可取得[例："{token}"]。

3.範例
1.將「空氣品質監測小時值」以SiteId欄位排序，取得第0-1000筆資料：
https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000208?offset=0&limit=1000&sort=SiteId&format=json&token={token}

2.將「空氣品質監測小時值」以SiteId欄位排序，取得第1000-2000筆資料：
https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000208?offset=1000&limit=1000&sort=SiteId&format=json&token={token}
*-------------------------*
|方法二：透過「OPEN API」    |
*-------------------------*
1.格式
https://opendata.epa.gov.tw/api/v1/{DataID}/?skip={skip}&top={top}&format={format}

2.參數
{DataID}    資料代號，各資料頁面內透過連結可取得[例：]。
{format}    資料格式，可選擇 json、xml、csv[例：]。
{top}    取n筆資料，請填入數字，最大值為1000[例：]。
{skip}    跳過筆數，請填入數字[例：]。
{token}    資料下載驗證碼，「會員註冊」頁面進行登記後可取得[例："{token}"]。

3.範例
1.將「空氣品質監測小時值」以SiteId欄位排序，取得第0-1000筆資料：

https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000208?offset=0&limit=1000&sort=SiteId&format=json&token={token}

2.將「空氣品質監測小時值」以SiteId欄位排序，取得第1000-2000筆資料：

https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000208?offset=1000&limit=1000&sort=SiteId&format=json&token={token}

"""
#import webbrowser
import os
import csv
#import matplotlib.pylab as plt
import requests
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#初始設定
SetDirectory = './'

#攫取即時資訊的網址
OpenData_F1700736_P601 = "http://opendata.epa.gov.tw/webapi/Data/POP00049/?$filter=CNO%20eq%20%27F1700736%27%20and%20PolNo%20eq%20%27P601%27&$orderby=M_Time%20desc&$skip=0&$top=1000&format=csv"
OpenData_F1700736_P701 = "http://opendata.epa.gov.tw/webapi/Data/POP00049/?$filter=CNO%20eq%20%27F1700736%27%20and%20PolNo%20eq%20%27P701%27&$orderby=M_Time%20desc&$skip=0&$top=1000&format=csv"
OpenData_POP00048 = "https://opendata.epa.gov.tw/Data/Contents/POP00048/"
OpenData_POP00049 = "https://opendata.epa.gov.tw/Data/Contents/POP00049/"
OpenData_API = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv"

OpenData = [OpenData_F1700736_P601,OpenData_F1700736_P701,OpenData_POP00048,OpenData_POP00049]
#將網站上取得的內容儲存成temp.csv
filename = 'temp.csv'  
def getOpenData(Url,Savefile):
    print("----------------------------攫取即時資訊中------------------------------")
    URL = OpenData_F1700736_P601
    html = urlopen(Url)
    html.encoding = "utf-8"
    bsObj = BeautifulSoup(html,features="html.parser")
    list2 = bsObj.text.split("\n")

    print(list2[1])
    print(list2[2])
    print(list2[3])
    print("\n----------------------------成功攫取即時資訊------------------------------")
    
# 備份即時資訊
    with open(Savefile,'w') as file_object:
        for line in list2:
            #file_object.write(line.rstrip())
            file_object.write(line)
    
        print("\n@@@備份即時資訊>>temp.csv<<< @@@")

    return

getOpenData(OpenData_F1700736_P601, filename)

#為讓檔案頭資料更容易理解，將列表中的每個檔案頭及其位置列印出來
with open(filename) as f:
    
    reader = csv.reader(f)      #閱讀器物件從其停留的地方繼續往下讀取CSV檔案
    header_row = next(reader)   #每次都自動返回當前所處位置的下一行
    #print(header_row)   

    for index, column_header in enumerate(header_row):  #呼叫了enumerate()來獲取每個元素的索引及其值
        print(index, column_header)
    
    M_Vals = []  #預先建立一個新的空列表，為了是要將每天的最高溫用字串形式儲存起來
    
    for row in reader:
        #highs.append(row[1]) #這個迴圈將從第二行開始,從這行開始包含的是"Max_Temperature"實際資料
        M_Val = row[7][3]     #使用int()將這些字串轉換為數字，讓matplotlib能夠讀取它們
        M_Vals.append(M_Val)
    print(M_Vals)

