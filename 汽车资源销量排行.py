from numpy import true_divide
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
from tqdm import tqdm

#网站https://www.evpartner.com/DAAS/Home/GetSalesRankingCar?year=2021&month=9&brandName=&carName=&page=1
#变的就是year，month和page

#1. 获取网页url
#for year in (2017,2022):
    #for month in (1,13):

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'}
#定义爬虫函数
def getdata(url):
    #获取网页请求
    html = requests.get(url,headers=headers)
    #2. 美丽汤，获取数据
    dataplus = html.json()  #json数据,是字典形式
    #dataplus = json.loads(dataplus, encoding='utf-8') #转化为字典形式
    return dataplus

type=[]
name=[]
brand=[]
sales=[]
proportion=[]
mon=[]
yr=[]
cumu=[]

#url='https://www.evpartner.com/DAAS/Home/GetSalesRankingCar?year=2017&month=8&brandName=&carName=&page=1'
#test= getdata(url)
#print(test)
#print(test['CheXingTable'][0]['PowerTypeName'])
#print(type(test))#字典形式
#print(test['Year'])
#print(len(test['CheXingTable'])) #是15行

#for i in range(len(test['CheXingTable'])):
    #yr.append(test['CheXingTable'][i]['Year'])
    #mon.append(test['CheXingTable'][i]['Month'])
    #type.append(test['CheXingTable'][i]['PowerTypeName'])
    #brand.append(test['CheXingTable'][i]['BrandName'])
    #name.append(test['CheXingTable'][i]['DataName'])
    #sales.append(test['CheXingTable'][i]['Sales'])
    #proportion.append(test['CheXingTable'][i]['Proportion'])
    #cumu.append(test['CheXingTable'][i]['CumulativeSales'])

#middata = {"年份": yr, "月份": mon, '燃油类型': type, '品牌': brand, '车型名称': name,'销量':sales, '占比': proportion, '累计': cumu}
#middata= pd.DataFrame(middata)
#成功

#
year=20
month=6
for year in tqdm(range(21,22)):
    for month in tqdm(range(1,13)):
        type=[]
        name=[]
        brand=[]
        sales=[]
        proportion=[]
        mon=[]
        yr=[]
        cumu=[]
        if month <10:
            monthNum = f'20{year}0{month}'
        else:
            monthNum = f'20{year}{month}'

        page=1
        while True:
            url1=f'https://www.evpartner.com/DAAS/Home/GetSalesRankingCar?year=20{year}&month={month}&brandName=&carName=&page={page}'
        #设置if语句，当dataplus没有数值是退出循环
            dataplus = getdata(url1)
            if len(dataplus['CheXingTable'])==0:
                break 
            else:
                for i in range(len(dataplus['CheXingTable'])):
                    yr.append(dataplus['CheXingTable'][i]['Year'])
                    mon.append(dataplus['CheXingTable'][i]['Month'])
                    type.append(dataplus['CheXingTable'][i]['PowerTypeName'])
                    brand.append(dataplus['CheXingTable'][i]['BrandName'])
                    name.append(dataplus['CheXingTable'][i]['DataName'])
                    sales.append(dataplus['CheXingTable'][i]['Sales'])
                    proportion.append(dataplus['CheXingTable'][i]['Proportion'])
                    cumu.append(dataplus['CheXingTable'][i]['CumulativeSales'])
            page+=1
        finaldata = {"年份": yr, "月份": mon, '燃油类型': type, '品牌': brand, '车型名称': name,'销量':sales, '占比': proportion, '累计': cumu}
        finaldata = pd.DataFrame(finaldata)

        if finaldata.shape[0]==0:
            break
        else:
            finaldata.to_csv(f'/Users/hanhaidi/Desktop/销量排行按车型/{monthNum}.csv',index=False)
        #finaldata.to_csv(f'/Users/hanhaidi/Desktop/销量排行按车型/{monthNum}.csv',index=False)
    
        



