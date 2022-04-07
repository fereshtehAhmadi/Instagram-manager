def login(driver):
    user_name = driver.find_element_by_name('username')
    user_name.send_keys(input("Enter your user name: "))
    
    password = driver.find_element_by_name('password')
    password.send_keys(input("Enter your password: "))
    
    login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
    