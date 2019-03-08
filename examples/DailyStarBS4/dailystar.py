import bs4
import requests

starUrl = "https://www.thedailystar.net/"
starPage = requests.get(starUrl).text

soup = bs4.BeautifulSoup(starPage, "html.parser")

left_bar = soup.select('h5 a')

for item in left_bar:
    print(item.text)

