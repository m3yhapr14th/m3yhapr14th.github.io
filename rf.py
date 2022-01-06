import requests
from bs4 import BeautifulSoup

cert_url = requests.get("https://www.krcert.or.kr/data/secNoticeList.do")
soup = BeautifulSoup(cert_url.text, "html.parser")
page_get = soup.find("div", {"class":"paging rwdP"})
table_get = soup.find("table", {"class":"basicList default"})