import requests as rq
from bs4 import BeautifulSoup
import re
url = "https://en.wikipedia.org/wiki/Buzzword"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = rq.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(response.text,'html.parser')
text = " ".join(p.get_text() for p in soup.find_all("p"))
words = re.findall(r'[a-zA-Z]+', text)
word = [w.lower() for w in words]
w = list(set(word))
print(w)