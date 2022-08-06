import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

for i in range(1,115):
    url = f"https://equran.me/read-{i}.html"
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "lxml")
    rev_div = soup.findAll("div", attrs={"class","ReadAya"})
    # soup = soup.find(text=True).strip()
    print(rev_div[0].find("ul").text)
    aya = rev_div[0].find("ul").text.strip()
    with open(f"data/{i}.text", "w", encoding="utf-8") as f:
        f.write(aya)