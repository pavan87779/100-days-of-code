from bs4 import BeautifulSoup
import requests
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
y_webiste = response.text
soup = BeautifulSoup(y_webiste, "html.parser")
print(soup.prettify())

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for tag in articles:
    text = tag.getText()
    article_texts.append(text)
    link = tag.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="spam", class_="score")]

print(article_texts)
print(article_links)
print(int(article_upvotes[0].split()[0]))

