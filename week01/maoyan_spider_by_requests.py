import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://maoyan.com/films?showType=3"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*",
    "Accept-Encoding": "gzip, deflate",
    "Dnt": "1",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": 'uuid_n_v=v1; uuid=D3F3ABB0CCFF11EAB0594FFAA70EE9CE992E7740FAFC4FA3AC3E78578E17132B; _csrf=4b94dc7d886b67d5d98ac3cd92ae54756deb0929701149927efbd4feb072ce4e; _lxsdk_cuid=1737c75fe2cc8-065a78fe4d7979-31617402-232800-1737c75fe2cc8; _lxsdk=D3F3ABB0CCFF11EAB0594FFAA70EE9CE992E7740FAFC4FA3AC3E78578E17132B; mojo-uuid=7137f97ef2cc97290d1dc1d484a19007; mojo-session-id={"id":"f1a20cfcc9425b43f41e2246ae214dd8","time":1595520975197}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595520975,1595520988; mojo-trace-id=12; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595521026; __mta=146519947.1595520975189.1595521015332.1595521026460.8; _lxsdk_s=1737c75fe2d-9f-ab2-76c%7C%7C21'
}

movie_data = {"movie_name":[], "movie_type": [], "movie_showtime": [] }
r = requests.get(url, headers=headers)
if not r.ok:
    exit(1)
bs_info = bs(r.text, 'html.parser')
count = 0 
for movie_info in bs_info.find_all('div', attrs={"class":"movie-hover-info"}):
    divs = movie_info.find_all('div', attrs={"class":"movie-hover-title"})
    movie_name = divs[0].find('span', attrs={"class":"name"}).text.strip()
    movie_type = divs[1].text.strip().split()[1]
    movie_showtime = divs[3].text.strip().split()[1]
    movie_data["movie_name"].append(movie_name)
    movie_data["movie_type"].append(movie_type)
    movie_data["movie_showtime"].append(movie_showtime)

    count += 1 
    if count >= 10:
        break
        
df = pd.DataFrame(data=movie_data)
df.to_csv('maoyan_movies.csv')