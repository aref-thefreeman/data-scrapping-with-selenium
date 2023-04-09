from selenium import webdriver
import time
from selenium import webdriver
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
# print(course_list)
# find the dynamic course title div
dynamic_title_div = course_list.find_element('class name', 'course-dynamic-title')
# print(dynamic_title_div)

# extract the text inside the a tag of the dynamic course title div
dynamic_title_link = dynamic_title_div.find_element('tag name', 'a')
# print(dynamic_title_link)

dynamic_title = dynamic_title_link.text
print(f'{dynamic_title}')

# close the browser window
browser.quit()
