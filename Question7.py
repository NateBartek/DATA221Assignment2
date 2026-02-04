# these are my imports
from bs4 import BeautifulSoup
import requests

# these are my headers to bypass restrictions
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# url for the data science wikipedia page
url = "https://en.wikipedia.org/wiki/Data_science"

# using requests and beatuiful soup to get the html and parse the information
data_science_html = requests.get(url, headers=headers)
data_science_soup = BeautifulSoup(data_science_html.text, "html.parser")

# getting the title as a string and printing it
title = data_science_soup.title.string
print(f"The title of the page is: {title}")

# finding the mw-content-text and finding all paragraphs
main_content = data_science_soup.find(id="mw-content-text")
main_paragraphs = main_content.find_all("p")

# loops through all elements in the main paragraphs to get text and remove leading and trailing whitespaces
# then it checks to make sure that there are at least 50 characters in the paragraphs because the website has at least one paragraph that doesn't contain anything (blanks)
# then it prints and breaks out of the loop
for paragraphs in main_paragraphs:
    text = paragraphs.get_text().strip()

    if len(text) >= 50:
        print(f"First Paragraph: {text}")
        break
