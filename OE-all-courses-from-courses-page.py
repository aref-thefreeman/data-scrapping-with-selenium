from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

# specify the path to chromedriver.exe
chrome_driver_path = 'C:/Users/mdare/Downloads/chromedriver_win32_111/chromedriver.exe'

# create a new Service object
service = Service(executable_path=chrome_driver_path)

# create a new Chrome browser instance
browser = webdriver.Chrome(service=service)

# navigate to the website you want to scrape
url = 'https://www.oneeducation.org.uk/courses/'
browser.get(url)
# wait for 5 seconds for the page to load
# time.sleep(5)

# find the course list container
course_list = browser.find_element('id', 'course-list')
# find all the course title list items
course_items = course_list.find_elements('class name', 'course-dynamic-title')

# loop through the course title list items and extract the title text
for item in course_items:
    dynamic_title_link = item.find_element('tag name', 'a')
    dynamic_title = dynamic_title_link.text
    print(f'{dynamic_title}')


pagination_div = browser.find_element('id', 'course-dir-pag-top')
page_numbers = pagination_div.find_elements('class name', 'page-numbers')
last_page_number = page_numbers[-2].text
print(f'Last Page Number: {last_page_number}')

# close the browser window
browser.quit()
