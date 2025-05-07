import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movie_titles = []

for title_tag in soup.find_all(name="h3", class_="title"):
    movie_titles.append(title_tag.get_text())

movie_titles.reverse()
# or movie_titles[::-1]

with open("/Day 45 Web Scraping/Starting+Code+-+100+movies+to+watch+start/Starting Code - 100 movies to watch start/movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
print("Movie titles have been written to movies.txt")
