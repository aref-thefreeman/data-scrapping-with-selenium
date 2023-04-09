from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# define a function to add course titles to the sheet
def add_course_titles(course_items, sheet):
    for item in course_items:
        dynamic_title_link = item.find_element('tag name', 'a')
        dynamic_title = dynamic_title_link.text
        print(f'{dynamic_title}')
        # add the title to the sheet
        sheet.append_row([dynamic_title])

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

# authenticate and open the Google Sheet
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('peppy-amplifier-383220-6ad59291424c.json', scope)
# peppy-amplifier-383220-6ad59291424c
client = gspread.authorize(creds)
sheet = client.open('Course Titles').sheet1

# add course titles to the sheet
add_course_titles(course_items, sheet)

while True:
    pagination_div = browser.find_element('id', 'course-dir-pag-top')
    next_button = pagination_div.find_element('class name', 'next')
    if next_button.get_attribute('href'):
        next_button.click()
        time.sleep(5)
        course_list = browser.find_element('id', 'course-list')
        course_items = course_list.find_elements('class name', 'course-dynamic-title')
        # add course titles to the sheet
        add_course_titles(course_items, sheet)
    else:
        break

# close the browser window
browser.quit()
