"""
 Copyright (C) 2022 Hemant Sachdeva <hemant.evolver@gmail.com>

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
 """


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

option = Options()
option.add_argument('--headless')  # Don't show the browser window


driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=option)


def get_phet_data(topic):

    driver.get(
        f'https://phet.colorado.edu/en/simulations/filter?subjects={topic}&type=html,prototype')

    titles = list()
    for element in driver.find_elements(By.CLASS_NAME, 'title'):
        text = element.text
        titles.append(text)

    embed_urls = list()
    for element in driver.find_elements(By.CSS_SELECTOR, 'a.tile'):
        link = element.get_attribute('href')
        link = link.replace('/en/simulations/', '/sims/html/') + \
            '/latest/' + link.split('/')[-1] + '_en.html'
        embed_urls.append(link)

    thumbnail_urls = list()
    for element in driver.find_elements(By.CSS_SELECTOR, 'img.thumbnail'):
        link = element.get_attribute('src')
        thumbnail_urls.append(link)

    data = dict()
    for i in range(len(titles)):
        data[i] = {
            'title': titles[i],
            'thumbnail_url': thumbnail_urls[i],
            'embed_url': embed_urls[i]
        }

    driver.quit()
    return data


if '__main__' == __name__:
    topic = 'math'
    data = get_phet_data(topic)
    print('Scraping Done')
    exit(0)