import time
from art import *
import text2art
from selenium import webdriver
from selenium.webdriver.common.keys import Keys;


#Facebook Auto Login With AUto Message sending feature

print(text2art("Script By Evan"));
driver = webdriver.Chrome();
driver.get("https://www.facebook.com/messages/");
el = driver.find_element_by_id("email");
user = input("Enter username");
el.send_keys(user);
passWord = input("Enter password");
el = driver.find_element_by_id("pass");
el.send_keys(passWord);
el.send_keys(Keys.RETURN);
print("Loading Complete");
time.sleep(40);
print("Sending Messages");
msg = driver.find_element_by_css_selector("._1mf");
print("Start");
for i in range(43):
	M = input("Enter message");
	msg.send_keys(M+Keys.RETURN);
	msg = driver.find_element_by_css_selector("._1mf");
	
	
