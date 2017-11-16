# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time
driver=webdriver.PhantomJS()
driver.get('http://www.renren.com/SysHome.do')
time.sleep(2)
driver.find_element_by_id('email').send_keys('18755870538')
driver.find_element_by_id('password').send_keys('')
driver.find_element_by_id('login').click()
time.sleep(1)
driver.save_screenshot('douban.png')
print driver.current_url
driver.quit()
