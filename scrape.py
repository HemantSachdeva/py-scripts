#!/usr/bin/env python3
import sys
try:
    import requests
    from requests_html import HTML
except ImportError:
    sys.exit("[!] Please make sure you have installed requests and requests_html module")


def url_to_scrap(url, filename="scrapped_data.html"):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            html_text = r.text
            with open(filename, "w") as f:
                f.write(html_text)
            return html_text
        else:
            return None
    except requests.exceptions.ConnectionError:
        return None


def parse_html(html_text):

    # find table with class imdb-scroll-table-inner in html
    table = html_text.find(".imdb-scroll-table-inner")

    # find all rows in table
    if len(table) == 1:
        parsed_table = table[0]
        rows = parsed_table.find("tr")

        # 1st row is header
        header = rows[0]
        header_cells = header.find("th")
        header_cells_text = [cell.text for cell in header_cells]
        print(header_cells_text)

        # 2nd row onwards are data rows
        for row in rows[1:]:
            row_data = row.find("td")
            row_values = [x.text for x in row_data]
            print(row_values)
    else:
        print("[!] Error parsing table")
        sys.exit(1)


if __name__ == "__main__":
    URL = "https://www.boxofficemojo.com/year/world/"
    html_text = url_to_scrap(URL)
    if html_text:
        print("[+] Scrapped data saved in scrapped_data.html")
        parse_html(HTML(html=html_text))
    else:
        print("[!] Unable to scrap data")
