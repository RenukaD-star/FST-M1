from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
with webdriver.Firefox() as driver:
    driver.get("http://alchemy.hguy.co/crm")

    userName = driver.find_element(By.ID,"user_name")
    userName.send_keys("admin")
    
    password = driver.find_element(By.ID,"username_password")
    password.send_keys("pa$$w0rd")
	
    login = driver.find_element(By.ID,"bigbutton")
    login.click()

    salesButton = driver.find_element(By.XPATH,"//*[@id=\"grouptab_0\"]")
    actions = ActionChains(driver)
    actions.move_to_element(salesButton).perform()

    wait = WebDriverWait(driver, 10)
    accounts = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"moduleTab_9_Accounts\"]")))
    accounts.click()

    wait = WebDriverWait(driver, 30)
    accountsTable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".list")))
    rows = accountsTable.find_elements(By.TAG_NAME,"tr")
    print(f"Total rows (including headers): {len(rows)}")

    nameCount = 0
    rowNumber = 1

    for i in range(2, len(rows)):
        row = rows[i]

        cells = row.find_elements(By.TAG_NAME, "td")


        if not cells:
            continue

        name = cells[2].text

        if not name or name == "(1 - 20 of 54)":
            continue  


        if rowNumber % 2 != 0:  
            print("Name:", name)
            nameCount += 1  

    
            if nameCount == 5:
              break  

        rowNumber += 1  

driver.quit()
 

