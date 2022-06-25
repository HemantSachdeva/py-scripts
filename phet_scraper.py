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


from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

option = Options()
option.add_argument('--headless')  # Don't show the browser window


driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=option)

driver.get(
    'https://phet.colorado.edu/en/simulations/filter?subjects=physics&type=html,prototype')

texts = list()
for element in driver.find_elements(By.CLASS_NAME, 'title'):
    text = element.text
    texts.append(text)

links = list()
for element in driver.find_elements(By.CSS_SELECTOR, 'a.tile'):
    link = element.get_attribute('href')
    link = link.replace('/en/simulations/', '/sims/html/') + \
        '/latest/' + link.split('/')[-1] + '_en.html'
    links.append(link)

data = dict()
for i in range(len(texts)):
    data[f'{texts[i]}'] = links[i]

pprint(data)
