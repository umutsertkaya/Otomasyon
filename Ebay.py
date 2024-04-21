from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import re

class Ebay_Data:
    def electronics():
        url = "https://www.ebay.com/globaldeals/trending/tech"
        service = webdriver.FirefoxService(r'C:/Drivers/geckodriver.exe')
        option = webdriver.FirefoxOptions()
        option.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        #option.add_argument("--headless")
        driver = webdriver.Firefox(service=service, options=option)
        json_data_list = []
        driver.get(url)
        time.sleep(20)
    
    
        last_height = driver.execute_script("return document.body.scrollHeight")

        last_height = driver.execute_script("return document.body.scrollHeight")

        for _ in range(1):  
            for i in range(1, 45):  
                scroll_height = last_height / 10 * i
                driver.execute_script(f"window.scrollTo(0, {scroll_height});")
                time.sleep(0.5)  
   
            time.sleep(3)

   
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        main_div = driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/div/div")
        first_inner_div = main_div.find_elements(By.CLASS_NAME, "col")
        say = len(first_inner_div)
        id_temp = 0
   
        for fid in first_inner_div:
            try:
                if id_temp <= say:
                
                
                    name_inner_div = fid.find_element(By.XPATH, ".//div/div[2]/a/h3/span/span")
                                                                #/html/body/main/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/div/div/div
                    price_inner_div = fid.find_element(By.XPATH, ".//div/div[2]/div/span[1]")
                    product_url = fid.find_element(By.XPATH, ".//div/div[1]/a").get_attribute("href")
                    driver.execute_script("window.open(arguments[0], '_blank');", product_url)
                    new_tab = driver.window_handles[-1]
                    driver.switch_to.window(new_tab)
                    for _ in range(1):  
                        for i in range(1, 15):  
                            scroll_height = last_height / 10 * i
                            driver.execute_script(f"window.scrollTo(0, {scroll_height});")
                            time.sleep(0.5)  
   
                        time.sleep(0.5)

   
                        new_height = driver.execute_script("return document.body.scrollHeight")
                        if new_height == last_height:
                            break
                        last_height = new_height
                    driver.close()
                    time.sleep(0.5)
                    main_tab = driver.window_handles[0]
                    driver.switch_to.window(main_tab)
                    time.sleep(0.5)
                    data = {
                        "Product-Name: ": f"{name_inner_div.text}",
                        "Product-Price: ": f"{price_inner_div.text}",
                        

                    }
                    json_data_list.append(data)

                    id_temp += 1
                
            except Exception as e:
                pass
        json_object = json.dumps(json_data_list, indent=4)
        with open("ebay_bin.json", "w") as outfile:
            outfile.write(json_object)
        print(json_data_list)
        driver.quit()
    electronics()