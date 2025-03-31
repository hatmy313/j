import requests
from bs4 import BeautifulSoup
import random
while True:
  user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) BingPreview/91.0.864.59 Safari/537.36',
]

  name = random.choice([
    'page.php?id=',
    'trainers.php?id=',
    'article.php?ID=',
    'games.php?id=',
    'newsDetail.php?id=',
    'staff.php?id=',
    'products.php?id=',
    'news_view.php?id=',
    'opinions.php?id=',
    'pages.php?id=',
])

  headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"116.0.5845.72"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': random.choice(user_agents),
    'x-client-data': 'CN+AywEIr8PNAQ==',
}

  params = {
    'q': name,
    'oq': name,
    'sourceid': 'chrome-mobile',
    'ie': 'UTF-8',
}

  res = requests.get('https://www.google.com/search', params=params, headers=headers)
  soup = BeautifulSoup(res.text, 'html.parser')

  links = []

  try:
      with open("Sql.txt", "r") as f:
          Mahos = set(f.read().splitlines())
  except:
      Mahos = set()

  for link in soup.find_all('a', href=True):
      url = link['href']
      if (url.startswith('http://') or url.startswith('https://')) and 'google.com' not in url and url not in Mahos:
          links.append(url)

  if links:
      with open("Sql.txt", "a") as f:
          for url in links:
              print(url)
              f.write(url + '\n')
  else:
      print("Nothings found")