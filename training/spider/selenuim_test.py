"""
@author yaoxs@shukun.net
@date 2019/10/17 17:25
"""
from selenium import webdriver

driver = webdriver.Chrome()
base_url = 'https://www.baidu.com'
driver.get(base_url)