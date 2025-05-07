from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    articles_title_tag = article_tag.a
    article_text = articles_title_tag.getText()
    article_texts.append(article_text)
    article_link = articles_title_tag.get("href")
    article_links.append(article_link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ = "score")]

article_upvote.insert(19, 0)


print(article_texts)
print(article_links)
print(article_upvote)

for index_upvote in range(len(article_upvote)):
    if article_upvote[index_upvote] == max(article_upvote):
        print(f"Article with the most upvotes: {article_texts[index_upvote]}")
        print(f"Link: {article_links[index_upvote]}")
        print(f"Upvotes: {article_upvote[index_upvote]}")

# Law of Web Scraping
# You can't commercialise copyrighted content
# You can't scrape data behind authentication
# reCAPTCHA is a challenge-response test to tell humans and bots apart
# Ethics of Web Scraping
# Public API First
# Respect the Web Owner 
# Read robots.txt 
# Limit your Rate














# import lxml

# with open("./Day 45 Web Scraping/bs4-start/bs4-start/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# # HTML title
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)

# # All HTML
# # print(soup)
# # print(soup.prettify())

# # first tag
# # print(soup.a)
# # print(soup.li)
# # print(soup.p)

# # all tags
# # all_anchor_tags = soup.find_all(name="a")
# # # print(all_anchor_tags)
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name.getText())

# headings = soup.select(".heading")
# print(headings)


