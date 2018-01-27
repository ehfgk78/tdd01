from selenium import webdriver

browser = webdriver.Chrome('//home/learn/projects/crawler/driver/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title