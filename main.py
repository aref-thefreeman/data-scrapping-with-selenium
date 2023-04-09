from selenium import webdriver

# specify the path to chromedriver.exe
# chrome_driver_path = 'C:/Users/mdare/Downloads/chromedriver_win32/chromedriver.exe'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# specify the path to chromedriver.exe
chrome_driver_path = 'C:/Users/mdare/Downloads/chromedriver_win32_111/chromedriver.exe'

# create a new Service object
service = Service(executable_path=chrome_driver_path)

# create a new Chrome browser instance
browser = webdriver.Chrome(service=service)

# navigate to the website you want to scrape
url = 'http://example.com/'
browser.get(url)

# find the div element
div_element = browser.find_element('tag name', 'div')

# get the text inside the h1 and p tags
h1_text = div_element.find_element('tag name', 'h1').text
p_text = div_element.find_element('tag name', 'p').text

# print the extracted text to the console
# print("h1 text: ", h1_text)
# print("p text: ", p_text)

# create a new file named 'output.txt' and write the extracted text to it
with open('output.txt', 'w') as f:
    f.write(f'Title: {h1_text}\n')
    f.write(f'Paragraph: {p_text}\n')

# close the browser window
browser.quit()
