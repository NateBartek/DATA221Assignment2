# these are my imports that i used
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

# identifying and then finding all of the HTML h2's wihtin the id mw-content-text
main_content = data_science_soup.find(id="mw-content-text")
main_h2 = main_content.find_all("h2")

# list to append the final h2 tags into
final_main_h2 = []

# list of the headings that we can't have included in the h2 tags
excluded_headings = ["References", "External links", "See also", "Notes"]


# loop to clean and check every h2 tag to make sure that it doesn't have the excluded headings inside of them
for h2 in main_h2:

    cleaned_h2 = h2.get_text().replace("[edit]", "").strip()

    if cleaned_h2 not in excluded_headings :
        final_main_h2.append(cleaned_h2)
        print()
    else:
        pass

# creates and writes to a new heading page with the cleaned headings
with open ("headings.txt", "w") as headings_page:

    for final_h2 in final_main_h2:
        headings_page.write(f"{final_h2} \n")