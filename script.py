#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from tqdm import tqdm_notebook
driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")

name = input("Enter the name of the chat or the group: ")
msg = input("Enter the message: ")
count = int(input("Enter the number of times: "))

a=input("Press enter after scanning")


user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

for i in tqdm_notebook(range(count)):
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
    button.click()
    
print("Done")

