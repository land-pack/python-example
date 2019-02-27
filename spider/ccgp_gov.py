import re
import requests
from bs4 import BeautifulSoup


target = "http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1&start_time=&end_time=&timeType=2&searchparam=&searchchannel=0&dbselect=bidx&kw=%E5%8D%B0%E5%88%B7&bidSort=0&pinMu=0&bidType=0&buyerName=&projectId=&displayZone=&zoneId=&agentName="
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



r = requests.get(target, headers=headers)

if __name__ == '__main__':
    if r.status_code == 200:
        #print(len(r.content))
        data = r.content
        soup = BeautifulSoup(data)
        #print(soup)
        #key = soup.find("div",class_="vT-srch-result-list-bid").p
        #key = soup.find("div",class_="vT-srch-result-list-bid")
        key = soup.find("div",class_="vT-srch-result-list")
        #key = soup.findAll("div", {"class": "vT-srch-result-list-bid"})
        #print(key)
        li = key.select("li")

        for i in li:
            title_s = i.select_one("p")
            link_s = i.select_one("a")
            title = re.search(r'<p>(.*?)</p>', str(title_s)).group(1)
            link = re.search(r'<a href=(.*?)style', str(link_s)).group(1)
            print(title)
            print(link)
    else:
        print("Failure to fecth the content: {}".format(r.status_code))


