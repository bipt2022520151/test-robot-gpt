import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    # 发起GET请求获取网页内容
    response = requests.get(url)
    if response.status_code == 200:
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(response.content, 'html.parser')

        # 查找具有 class="bd1" 的表格元素
        table = soup.find('table', class_='bd1')
        # print(table)
        rows = table.find_all('tr')
        for i in rows:
            a = i.find_all('td')
            for j in a:
                print(j)


# 调用爬虫函数并传入目标网页的URL
url = "https://www.most.gov.cn/xxgk/xinxifenlei/fdzdgknr/fgzc/gfxwj/gfxwj2022/202301/t20230116_184248.html"
scrape_website(url)
