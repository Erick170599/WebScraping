from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')

matches = driver.find_elements_by_tag_name('tr')

partidos = []
for match in matches:
    partidos.append(match.text)

driver.quit()

df = pd.DataFrame({'Partidos': partidos })
print(df)
df.to_csv('Partidos.csv', index=False)