import sys
import requests

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*",
    "Accept-Encoding": "gzip, deflate",
    "origin": "https://shimo.im",
    "referer": "https://shimo.im/login?from=home",
    "x-requested-with": "XmlHttpRequest",
    "x-source": "lizard-desktop"
}

url = "https://shimo.im/lizard-api/auth/password/login"
data = {
        "email":"120xxx@qq.com",
        "mobile": "+86undefined",
        "password": "TEST000"
       }

s = requests.Session()
r = s.post(url, headers = headers,
      data = data)

if not r.ok:
   print(r.status_code)
   print(r.text)
   sys.exit(1)

url_myprofile = "https://shimo.im/lizard-api/users/me"
myprofile = s.get(url_myprofile, headers = headers)
print(myprofile.json())