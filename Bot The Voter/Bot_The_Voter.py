while True:
    from ast import arguments
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import pyautogui
    import time
    import random
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    #driver.maximize_window()
    driver.get("https://events.skeducations.com/DigitalEvents/carnivalShare?bcuid=Mjk5")
    time.sleep(4)
    votebtn= driver.find_element_by_class_name("need_login")
    driver.execute_script("arguments[0].click();",votebtn)
    time.sleep(1)
    name= driver.find_element_by_name("name")
    name.click()
    name.send_keys("pillolo")
    email=driver.find_element_by_name("email")
    email.click()
    unamelist = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    uname=(random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+"@guko.sf")
    email.send_keys(uname)
    mobile_no=driver.find_element_by_name("mobile_no")
    mobile_no.click()
    mobile_no.send_keys("6878474897")
    submit=driver.find_element_by_id("updateCarnivalAuth")
    submit.click()
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(3)
    like= driver.find_element_by_class_name("up_like")
    driver.execute_script("arguments[0].click();",like)
    time.sleep(3)
    driver.quit()


