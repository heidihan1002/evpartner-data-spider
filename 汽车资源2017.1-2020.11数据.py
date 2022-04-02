#from calendar import month
#from pkgutil import extend_path
#from traceback import format_tb
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
from  datetime  import  *

#网站https://www.evpartner.com/daas/

#1. 获取网页url
url ='https://www.evpartner.com/DAAS/Home/GetData'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'}
html = requests.post(url,headers=headers)
#2. 美丽汤，获取数据
data= html.json()  #json数据,是字典形式

#时间
month = []
year = []
lists = data['NewEnergyData']
for list in lists:
    month.append(list['Month'])
    year.append(list['Year'])
Time = {"年份": year, "月份": month}
time=pd.DataFrame(Time)

nevsale=[]
nevyields=[]
evsales=[]
evyields=[]
hevsales=[]
hevyields=[]

#新能源汽车产销
lists1 = data['NewEnergyData']
for list1 in lists1:
    nevsale.append(list1['Sales'])
    nevyields.append(list1['Yield'])
nev = {"新能源汽车产量": nevyields, "新能源汽车销量": nevsale}
nev=pd.DataFrame(nev)


#纯电动汽车
lists2 = data['PureElectricData']
for list2 in lists2:
    evsales.append(list2['Sales'])
    evyields.append(list2['Yield'])
ev = {"纯电动汽车产量": evyields, "纯电动汽车销量": evsales}
ev=pd.DataFrame(ev)


#插电式混动汽车
lists3 = data['HybridData']
for list3 in lists3:
    hevsales.append(list3['Sales'])
    hevyields.append(list3['Yield'])
hev = {"插电式混动汽车产量": hevyields, "插电式混动汽车销量": hevsales}
hev=pd.DataFrame(hev)


finaldata= pd.concat([time,nev,ev,hev], axis=1)
print(finaldata)
finaldata.to_csv("/Users/hanhaidi/Desktop/20172020aggregatedata.csv",index=False)
