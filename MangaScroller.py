import keyboard
import string
import time
from selenium import webdriver
             
print("What would you like to read?")

manga = input()

global y
y = 750

#while the page is above the bottom
while y < 40000:
    global y_multiple
    y_multiple = 10
    #open chrome, assign height a value, and scroll by y each time it resets
    driver = webdriver.Chrome()
    driver.get(str(manga))
    height = driver.execute_script("return document.body.scrollHeight")
    for timer in range(0,1000):
             driver.execute_script("window.scrollTo(0, "+str(y)+")")
             y += y_multiple
             if keyboard.is_pressed('w'):
                 y_multiple += 10
             if keyboard.is_pressed('s'):
                 y_multiple -= 10
             if y > 40000:
                print("Reading is complete. Closing in 3 seconds")
                driver.quit()
                time.sleep(3)
                quit()
                
             time.sleep(0.05)
    time.sleep(0.1)

    
