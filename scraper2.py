import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", {"class": "wikitable"})
rows = table.find_all("tr")

data = []
for row in rows[1:]:
    cols = row.find_all("td")
    star_name = cols[0].text.strip()
    mass = cols[7].text.strip()
    radius = cols[8].text.strip()
    distance = cols[5].text.strip()
    data.append([star_name, mass, radius, distance])

df = pd.DataFrame(data, columns=["Star Name", "Mass", "Radius", "Distance"])
df.to_csv("brown_dwarfs.csv")
