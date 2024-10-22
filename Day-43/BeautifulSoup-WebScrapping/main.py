
from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()
soup = BeautifulSoup(content,"html.parser")
print(soup.title.string)

print(soup.prettify())
print(soup.p)

all_anchor = soup.find_all(name = "a")
print(all_anchor)
for tag in all_anchor:

    print(tag.getText("href") +" " + tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3")
print(section_heading.string)