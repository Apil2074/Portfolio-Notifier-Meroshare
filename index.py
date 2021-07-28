from typing import final
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pyautogui
from plyer import notification


passe = int(input('Enter your password'))

# //*[@id="select2-ycn1-container"]
# Executing Chrome driver0
driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')

driver.get('https://meroshare.cdsc.com.np/#/login')
driver.minimize_window
()
time.sleep(0.1)

# Entering the bank detail fo the stock holder


bankey = driver.find_element_by_xpath(
    '/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div')
bankey.click()
time.sleep(0.1)
# bankey.send_keys('mac')
# s1 = Select(driver.find_element_by_xpath('/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/select/option[34]'))
# thisss = bankey.select_by_visible_text('MACHHAPUCHCHHRE BANK LIMITED (16100)')
pyautogui.write('mac')
pyautogui.press('Enter')
time.sleep(0.1)
# searchselects = Select(thisss)


time.sleep(0.1)


usname = driver.find_element_by_xpath(
    '/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[2]/div/div/input')

usname.send_keys('00548341')
# elem.select_by_visible_text("MACHHAPUCHCHHRE BANK LIMITED (16100)")
psname = driver.find_element_by_xpath('//*[@id="password"]')
psname.send_keys(passe)
buttonclic = driver.find_element_by_xpath(
    '/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button')
buttonclic.click()
time.sleep(0.1)
# clicking the my portfolio option
time.sleep(0.5)
poclick = driver.find_element_by_xpath('//*[@id="sideBar"]/nav/ul/li[5]/a')
poclick.click()
time.sleep(0.5)
print(driver.find_element_by_xpath(
    '//*[@id="main"]/div/app-my-portfolio/div/div[2]/div/div/table/tbody[1]/tr[1]/td[1]').get_attribute('innerHTML'))
time.sleep(0.2)

link_tags = driver.find_elements_by_tag_name('tr')
tdr = driver.find_elements_by_tag_name('td')
listss = []
time.sleep(0.1)
for td in link_tags:
    # print(td.get_attribute('innerHTML'))
    pass
for tdqe in tdr:
    
    # print (tdqe.get_attribute('innerHTML'))
    listss.append(tdqe.get_attribute('innerHTML'))
# print(listss)
newkef = listss[:7]
nifra = listss[7:12]
shel = listss[14:20]
print(*newkef)
print(*nifra)
print(*shel)
print2=('  '.join(newkef))
print3=('  '.join(nifra))
print4=('  '.join(shel))
finalprint = (print4)

final_list= [print2, print3, print4]
for listey in final_list:
    notification.notify(
        title="Hey Mr Subedi your Current Holings are:",
        message= listey,
        timeout=3
    )
time.sleep(15)
driver.close()
