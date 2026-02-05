from bs4 import BeautifulSoup
import requests
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = "https://en.wikipedia.org/wiki/Machine_learning"

machine_learning_html = requests.get(url, headers=headers)
machine_learning_soup = BeautifulSoup(machine_learning_html.text, "html.parser")

main_content = machine_learning_soup.find(id="mw-content-text")
main_table = main_content.find_all("table")

first_table = None

for table in main_table:
    if len(table.find_all("tr")) >= 3:
        first_table = table
        break

header_cells = first_table.find_all("th")
header_text = []

for th in header_cells:
    clean_headers = th.get_text()

    header_text.append(clean_headers)

rows = first_table.find_all("tr")
table_data = []

for row in rows[1:]:
    cells = row.find_all(["td", "th"])
    row_data = []
    for cell in cells:
        row_data.append(cell.get_text())
    while len(row_data) < len(header_text):
        row_data.append("")
    table_data.append(row_data)

with open("wiki_table.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(header_text)
    writer.writerow(table_data)
