    # dfs.to_csv(r'D:\Work program\python\%s.csv'% (str(city)),mode='a+',encoding='utf_8_sig')

# coding=utf-8
from selenium import webdriver
# import pymysql
import pandas as pd
import time
import requests
import re
from bs4 import BeautifulSoup
# from sqlalchemy.exc import IntegrityError

def get_date(url):
    response = requests.get(url)
    dates = []
    try:
        if response.status_code ==200:
            response = response.text
            soup = BeautifulSoup(response, 'lxml')
            dates_ = soup.find_all('li')
            for i in dates_:
                if i.a:  # 去除空值
                    li = i.a.text  # 提取li标签下的a标签
                    date = re.findall('[0-9]*', li)  # ['2019', '', '12', '', '']
                    year = date[0]
                    month = date[2]
                    if month and year:  # 去除不符合要求的内容
                        date_new = '-'.join([year, month])
                        dates.append(date_new)
            return dates
    except:
        print('数据获取失败！')
def spider(url):
    browser.get(url)
    df = pd.read_html(browser.page_source, header=0)[0]  # 返回第一个Dataframe
    time.sleep(1.5)
    if not df.empty:
        print(df)
        df.to_csv('data.csv', mode='a', index=None)
        print(url+'数据爬取已完成')
        return df
    else:
        return spider(url)  # 防止网络还没加载出来就爬取下一个url
if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%8C%97%E4%BA%AC'
    base_url = 'https://www.aqistudy.cn/historydata/daydata.php?city='
    # 声明浏览器对象
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option("useAutomationExtension", False)
    browser = webdriver.Chrome(
        =option)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
        'source':'''Object.defineProperty(navigator, 'webdriver', {
        get: () =>false'''
    })
    city = [
        '北京',
            ]
    dates = get_date(url)[1:]
    print(dates)
    list_data = []
    list_row = []
    for ct in range(len(city)):
        for date in dates:
            url = base_url + city[ct] + '&month=' + date
            df = spider(url)
            # print(df)
            time.sleep(1.5)
            df['city'] = city[ct]  # 添加一列
            for i in range(0, df.shape[0]):  # 行
                for j in range(df.shape[1]):  # 列
                    data = df.iloc[i, j]
                    list_row.append(data)
                list_data.append(list_row)
                list_row = []
            print(list_data)
    browser.close()
    aqidata = pd.DataFrame(list_data,
                columns=['日期', 'AQI', '质量等级', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3_8h', 'city'])
    print('所有数据爬取已完成！\n', aqidata)
