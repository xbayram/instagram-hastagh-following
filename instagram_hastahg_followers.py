import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#xbayram copyright 2021-2024

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)


username = "username"#buraya hesabınızın kullanıcı adını girin. Enter your account username here.
usernameInput = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
time.sleep(1)
usernameInput.send_keys(username)

password = "password"#buraya hesabınızın şifresini girin. Enter your account password here.
passwordInput = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
time.sleep(1)
passwordInput.send_keys(password)

sendForm = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button")
sendForm.click()
time.sleep(6)

driver.get("https://www.instagram.com/")

degil2 = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
degil2.click()
time.sleep(5)

arama = "#france"#buraya takip etmek istediğiniz hastagh ismini girin. Enter the hastagh name you want to track here.
aramaInput = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
aramaInput.send_keys(arama)
time.sleep(2)

driver.get("https://www.instagram.com/explore/tags/france/")#buradaki "france" kelimesini yukarda belirttiğiniz hastahg ismi ile değiştirin. Replace the word "france" here with the hastagh name you specified above.

account = driver.find_element_by_xpath("/html/body/div[1]/section/main/header/div[2]/div/button")
account.click()
time.sleep(2)
