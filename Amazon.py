from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import re

class Amazon_Data:
    def electronics():
        url = "https://www.amazon.com.tr/gp/bestsellers/electronics/ref=zg_bs_electronics_sm"
        service = webdriver.FirefoxService(r'C:/Drivers/geckodriver.exe')
        option = webdriver.FirefoxOptions()
        option.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        option.add_argument("--headless")
        driver = webdriver.Firefox(service=service, options=option)
        json_data_list = []
        driver.get(url)
        time.sleep(10)
    
        main_div = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]")
        last_height = driver.execute_script("return document.body.scrollHeight")

        last_height = driver.execute_script("return document.body.scrollHeight")

        for _ in range(1):  
            for i in range(1, 15):  
                scroll_height = last_height / 10 * i
                driver.execute_script(f"window.scrollTo(0, {scroll_height});")
                time.sleep(0.5)  
   
            time.sleep(3)

   
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        first_inner_div = main_div.find_elements(By.ID, "gridItemRoot")
        say = len(first_inner_div)
        id_temp = 0
   
        for fid in first_inner_div:
            try:
                if id_temp <= say:
                
                
                    name_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/a[2]/span/div")
                    price_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[2]/div/div/a/div/span/span")
                    comment_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[1]/div/a/span")
                    rate_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[1]/div/a/i/span")
                    rate_inner_div_text = driver.execute_script("return arguments[0].textContent;", rate_inner_div)
                    rate_info = re.search(r'5 yıldız üzerinden (\d+\,\d+)', rate_inner_div_text)
                    if rate_info:
                        rate_info_value = rate_info.group(1)
                    else:
                        rate_info_value = ""
                    data = {
                        "Product-Name: ": f"{name_inner_div.text}",
                        "Product-Price: ": f"{price_inner_div.text}",
                        "Product-Comment: ": f"{comment_inner_div.text}",
                        "Product-Rate: ": f"{rate_info_value}"


                    }
                    json_data_list.append(data)

                    id_temp += 1
                
            except Exception as e:
                pass
        json_object = json.dumps(json_data_list, indent=4)
        with open("amazon_bin.json", "w") as outfile:
            outfile.write(json_object)
        print(json_data_list)
        driver.quit()
    def books():

        url = "https://www.amazon.com.tr/gp/bestsellers/books/ref=zg_bs_books_sm"
        service = webdriver.FirefoxService(r'C:/Drivers/geckodriver.exe')
        option = webdriver.FirefoxOptions()
        option.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        option.add_argument("--headless")
        driver = webdriver.Firefox(service=service, options=option)
        json_data_list = []
        driver.get(url)
        time.sleep(10)
        main_div = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]")
        last_height = driver.execute_script("return document.body.scrollHeight")

        last_height = driver.execute_script("return document.body.scrollHeight")

        for _ in range(1):  
            for i in range(1, 15):  
                scroll_height = last_height / 10 * i
                driver.execute_script(f"window.scrollTo(0, {scroll_height});")
                time.sleep(0.5)  
   
            time.sleep(3)

   
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        first_inner_div = main_div.find_elements(By.ID, "gridItemRoot")
        say = len(first_inner_div)
        id_temp = 0
   
        for fid in first_inner_div:
            try:
                if id_temp <= say:
                
                
                    name_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/a[2]/span/div")
                                                                #/div/div/div[2]/div/a[2]/span/div
                    price_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[4]/div/div/a/div/span/span")
                                                                #/div/div/div[2]/div/div[4]/div/div/a/div/span/span
                    comment_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[2]/div/a/span")
                                                                    #/div/div/div[2]/div/div[2]/div/a/span
                                                                    #/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]
                    rate_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[2]/div/a/i/span")
                                                                #/div/div/div[2]/div/div[2]/div/a/i/span
                                                                #.//div/div/div[2]/div/div[1]/span/div
                    author_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[1]/span/div")
                    author_inner_div_text = driver.execute_script("return arguments[0].textContent;", author_inner_div)
                    rate_inner_div_text = driver.execute_script("return arguments[0].textContent;", rate_inner_div)
                    rate_info = re.search(r'5 yıldız üzerinden (\d+\,\d+)', rate_inner_div_text)
                    if rate_info:
                        rate_info_value = rate_info.group(1)
                    else:
                        rate_info_value = ""
                    data = {
                        "Product-Name: ": f"{name_inner_div.text}",
                        "Product-Price: ": f"{price_inner_div.text}",
                        "Product-Comment: ": f"{comment_inner_div.text}",
                        "Product-Rate: ": f"{rate_info_value}",
                        "Author: ": f"{author_inner_div_text}"

                    }
                    json_data_list.append(data)

                    id_temp += 1
                
            except Exception as e:
                pass
        json_object = json.dumps(json_data_list, indent=5)
        with open("amazon_bin.json", "w") as outfile:
            outfile.write(json_object)
    

        driver.quit()
    def Fashion():
        url = "https://www.amazon.com.tr/gp/bestsellers/apparel/ref=zg_bs_nav_apparel_0"
        service = webdriver.FirefoxService(r'C:/Drivers/geckodriver.exe')
        option = webdriver.FirefoxOptions()
        option.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        option.add_argument("--headless")
        driver = webdriver.Firefox(service=service, options=option)
        json_data_list = []
        driver.get(url)
        time.sleep(10)
        main_div = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]")
                                                #.p13n-gridRow
                                                ##CardInstanceA7rNlvWoHEyonI_q_5JCgQ > div.a-cardui._cDEzb_card_1L-Yx > div.p13n-desktop-grid > div.p13n-gridRow._cDEzb_grid-row_3Cywl
        last_height = driver.execute_script("return document.body.scrollHeight")

        last_height = driver.execute_script("return document.body.scrollHeight")

        for _ in range(1):  
            for i in range(1, 15):  
                scroll_height = last_height / 10 * i
                driver.execute_script(f"window.scrollTo(0, {scroll_height});")
                time.sleep(0.5)  
   
            time.sleep(3)

   
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        first_inner_div = main_div.find_elements(By.ID, "gridItemRoot")
        say = len(first_inner_div)
        id_temp = 0
        for fid in first_inner_div:
            try:
                if id_temp <= say:
                
                
                    name_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/a[2]/span/div")
                                                                #/div/div/div[2]/div/a[2]/span/div
                                                               #/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]
                                                                #.//div/div/div[2]/div/div[2]/div/div/a/div/span/span
                    price_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[2]/div/div/a/div/span/span")
                                                                #/div/div/div[2]/div/div[2]/div/div/a/div/span/span
                    comment_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[1]/div/a/span")
                                                                    #.//div/div/div[2]/div/div[1]/div/a/span
                    rate_inner_div = fid.find_element(By.XPATH, ".//div/div/div[2]/div/div[1]/div/a/i/span")
                                                                #.//div/div/div[2]/div/div[1]/div/a/i/span
                   
                    rate_inner_div_text = driver.execute_script("return arguments[0].textContent;", rate_inner_div)
                    rate_info = re.search(r'5 yıldız üzerinden (\d+\,\d+)', rate_inner_div_text)
                    if rate_info:
                        rate_info_value = rate_info.group(1)
                    else:
                        rate_info_value = ""
                    data = {
                        "Product-Name: ": f"{name_inner_div.text}",
                        "Product-Price: ": f"{price_inner_div.text}",
                        "Product-Comment: ": f"{comment_inner_div.text}",
                        "Product-Rate: ": f"{rate_info_value}",
        

                    }
                    json_data_list.append(data)

                    id_temp += 1
                
            except Exception as e:
                pass
        json_object = json.dumps(json_data_list, indent=4)
        with open("amazon_bin.json", "w") as outfile:
            outfile.write(json_object)
       
        driver.quit()
    electronics()


                                         

    
    