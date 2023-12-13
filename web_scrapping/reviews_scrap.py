from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from amazoncaptcha import AmazonCaptcha
from database import get_database
from pymongo import MongoClient

def get_reviews_amazon(keyword):
    dbase = get_database()
    web = 'https://www.amazon.com'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    ##captcha solver

    try:
        img_div = driver.find_element(By.XPATH, "//div[@class = 'a-row a-text-center']//img").get_attribute('src')
        captcha = AmazonCaptcha.fromlink(img_div)
        captcha_value = AmazonCaptcha.solve(captcha)
        input_field = driver.find_element(By.ID, "captchacharacters").send_keys(captcha_value)
        button = driver.find_element(By.CLASS_NAME, "a-button-text")
        button.click()
    except:
        print("No captcha found")

    ##end captcha solver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(web)
    next_page = ''
    driver.implicitly_wait(5)
    # keyword = "Dark Horse Deluxe The Witcher III: The Wild Hunt:"
    # collection_name = dbase[keyword]
    search = driver.find_element(By.ID, 'twotabsearchtextbox')
    search.send_keys(keyword)
    # click search button
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()
    reviews = []
    driver.implicitly_wait(5)

    items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
    for item in items:
        # find ASIN number 
        title = item.find_element(By.XPATH,'.//span[@class="a-size-medium a-color-base a-text-normal"]')
        img_link = item.find_element(By.XPATH,'.//img[@class="s-image"]').get_attribute('src')
        data_asin = item.get_attribute("data-asin")
        product_asin = data_asin
        break
    web = "https://www.amazon.com/product-reviews/" + product_asin + "/"
    print(img_link)
    print(title.text)
    list_of_collections = dbase.list_collection_names()
    print(list_of_collections)
    if title.text in list_of_collections:
        print("Collection exists")
        collection = dbase[title.text]
        cursor = collection.find({})
        for document in cursor:
            reviews.append(cursor[document]["Review"])
        print(reviews)
        return 0
    else:
        print("Collection dose not exists")
    # try:
    #     dbase.validate_collection(title.text)  # Try to validate a collection
    # except pymongo.errors.OperationFailure:  # If the collection doesn't exist
    #     print("This collection doesn't exist")
    collection_name = dbase[title.text]
    title={"Product Name": title.text, "Product-img": img_link}
    collection_name.insert_one(title)
    print(web)
    driver.get(web)
    driver.implicitly_wait(5)
    count=1
    temp = 0
    insert = {}
    try:
        while True:
            items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "a-row a-spacing-small review-data")]')))
            for item in items:
                review = item.find_element(By.XPATH, './/span[@class="a-size-base review-text review-text-content"]')
                temp += 1
                insert ={"Review":review.text}
                print("No of reveiws:", temp)
                collection_name.insert_one(insert)
                reviews.append(review.text)
                if temp > 14:
                    print("temp executed inner loop")
                    break

            if temp > 14:
                print("temp executed outer loop")
                break

            try:
                next_page = driver.find_element("xpath","//li[contains(@class, 'a-last')]/a").get_attribute('href')
            except:
                print("Page End")
                break
            count += 1
            print("Page:",count)
            driver.get(next_page)
            driver.implicitly_wait(5)
    except:
        print("No reviews found")
    driver.quit()
    print(reviews)

if get_reviews_amazon("Portable monitor asus") == 0:
    print("reviews already collected")
else:
    print("reviews collected")