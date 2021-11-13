#!/usr/bin/env python3
import sys
try:
    import requests
except ImportError:
    sys.exit("[!] Please make sure you have installed requests module")


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


if __name__ == "__main__":
    URL = "https://www.boxofficemojo.com/year/world/"
    html_text = url_to_scrap(URL)
    if html_text:
        print("[+] Scrapped data saved in scrapped_data.html")
    else:
        print("[!] Unable to scrap data")
