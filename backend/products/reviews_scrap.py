# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.support import expected_conditions as EC
# from amazoncaptcha import AmazonCaptcha
# from .database import get_database
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# import time

# continue_exe = False
# driver = None
# dbase = None
# start = None


# def initialize_driver():

#     global driver
#     global dbase
#     global start
#     start = time.time()
#     database_name="Reviews"
#     dbase = get_database(database_name)
#     web = 'https://www.amazon.com'
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_experimental_option(
#         "prefs", {
#             # block image loading
#             "profile.managed_default_content_settings.images": 2,
#         }
#     )
#     # captcha solver
#     chrome_options = Options()
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument("--window-size=1920,1080")
#     chrome_options.add_argument('--ignore-certificate-errors')
#     chrome_options.add_argument('--allow-running-insecure-content')
#     options.add_argument('--disk-cache-dir=/path/to/cache')
#     user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
#     options.add_argument(f'user-agent={user_agent}')
#     # chrome_options.add_argument('--disable-dev-shm-usage')

#     # end captcha solver
#     driver = webdriver.Chrome(service=ChromeService(
#         ChromeDriverManager().install()), options=chrome_options)
#     driver.get(web)
#     captchaSolver()


# def captchaSolver():
#     global driver
#     try:
#         img_div = driver.find_element(
#             By.XPATH, "//div[@class = 'a-row a-text-center']//img").get_attribute('src')
#         captcha = AmazonCaptcha.fromlink(img_div)
#         captcha_value = AmazonCaptcha.solve(captcha)
#         input_field = driver.find_element(
#             By.ID, "captchacharacters").send_keys(captcha_value)
#         button = driver.find_element(By.CLASS_NAME, "a-button-text")
#         button.click()
#     except:
#         print("No captcha found")


# def get_reviews_amazon():
#     global start_pro
#     global continue_exe
#     global next_page
#     initialize_driver()
#     next_page = ''
#     driver.implicitly_wait(2)
#     # keyword = "Dark Horse Deluxe The Witcher III: The Wild Hunt:"
#     # collection_name = dbase[keyword]
#     print("waiting for keyword")
#     end = time.time()
#     print("time:", end-start)


# def after_func(keyword, scraping_done_event, results):
#     global next_page
#     global driver
#     global start
#     driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(keyword)
#     # click search button
#     search_button = driver.find_element(By.ID, 'nav-search-submit-button')
#     search_button.click()
#     reviews = []
#     driver.implicitly_wait(1)

#     items = wait(driver, 10).until(EC.presence_of_all_elements_located(
#         (By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
#     for item in items:
#         # find ASIN number
#         try:
#             title = item.find_element(
#                 By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')
            
#         except:
#             title = item.find_element(
#                 By.XPATH, './/span[@class="a-size-base-plus a-color-base a-text-normal"]')
#         # try:
#         #     price = item.find_element(By.XPATH, './/span[@class="a-price-whole"]')
#         # except:
#         #     print("Price not found")
#         img_link = item.find_element(
#             By.XPATH, './/img[@class="s-image"]').get_attribute('src')
#         data_asin = item.get_attribute("data-asin")
#         product_asin = data_asin
#         break
#     web = "https://www.amazon.com/product-reviews/" + product_asin + "/"
#     print(img_link)
#     print(title.text)
#     # print(price.text)
#     results[0] = title.text
#     list_of_collections = dbase.list_collection_names()
#     # print(list_of_collections)
#     if title.text in list_of_collections:
#         print("Collection exists")
#         # collection = dbase[title.text]
#         # cursor = collection.find({})
#         # for doc in cursor:
#         #     reviews.append(doc)
#         # while True:
#         #     try:
#         #         # print(reviews_arr[i]['Review'])
#         #         overall = overall + reviews[i]['Review']
#         #         i = i + 1
#         #     except:
#         #         break
#         # reviews = overall
#         # print(reviews)
#         scraping_done_event.set()
#         return title.text
#     else:
#         print("Collection dose not exists")
#     # try:
#     #     dbase.validate_collection(title.text)  # Try to validate a collection
#     # except pymongo.errors.OperationFailure:  # If the collection doesn't exist
#     #     print("This collection doesn't exist")
#     collection_name = dbase[title.text]
#     value = title.text
#     # title = {"product_name": title.text, "product_img": img_link, "product_price": price.text}
#     title = {"product_name": title.text, "product_img": img_link }
#     print(web)
#     driver.get(web)
#     captchaSolver()
#     driver.get_screenshot_as_file("screenshot.png")
#     driver.implicitly_wait(5)
#     count = 1
#     temp = 0
#     insert = {}
#     try:
#         collection_name.insert_one(title)
#         while True:
#             items = wait(driver, 10).until(EC.presence_of_all_elements_located(
#                 (By.XPATH, '//div[contains(@class, "a-row a-spacing-small review-data")]')))
#             for item in items:
#                 review = item.find_element(
#                     By.XPATH, './/span[@class="a-size-base review-text review-text-content"]')
#                 temp += 1
#                 insert = {"Review": review.text}
#                 # print("No of reveiws:", temp)
#                 collection_name.insert_one(insert)
#                 reviews.append(review.text)
#                 if temp > 14:
#                     print("temp executed inner loop")
#                     break

#             if temp > 14:
#                 print("temp executed outer loop")
#                 break

#             try:
#                 next_page = driver.find_element(
#                     "xpath", "//li[contains(@class, 'a-last')]/a").get_attribute('href')
#             except:
#                 print("Page End")
#                 break
#             count += 1
#             print("Page:", count)
#             driver.get(next_page)
#             driver.implicitly_wait(2)
#     except:
#         print("No reviews found")
#         return 0
#     driver.quit()
#     print(reviews)
#     end = time.time()
#     print("Total time is: ", end - start)
#     # print (value)

#     scraping_done_event.set()
#     return value


# get_reviews_amazon()
# after_func("lenevo thinkpad")
# print(get_reviews_amazon("Forza Motorsport – Standard Edition – Xbox Series X"))




from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from amazoncaptcha import AmazonCaptcha
from .database import get_database
from selenium.webdriver.chrome.options import Options
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_driver():
    global driver
    global dbase
    global start

    database_name="Reviews"
    print (database_name)

    start = time.time()
    dbase = get_database(database_name)
    web = 'https://www.amazon.com'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disk-cache-dir=/path/to/cache')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(web)
    captcha_solver()

def captcha_solver():
    global driver
    try:
        img_div = driver.find_element(By.XPATH, "//div[@class = 'a-row a-text-center']//img").get_attribute('src')
        captcha = AmazonCaptcha.fromlink(img_div)
        captcha_value = AmazonCaptcha.solve(captcha)
        input_field = driver.find_element(By.ID, "captchacharacters").send_keys(captcha_value)
        button = driver.find_element(By.CLASS_NAME, "a-button-text")
        button.click()
    except Exception as e:
        logger.error(f"Error in captcha_solver: {str(e)}")

def get_reviews_amazon():
    global start
    initialize_driver()
    driver.implicitly_wait(2)
    logger.info("Waiting for keyword")
    end = time.time()
    logger.info(f"Time: {end - start}")

def after_func(keyword, scraping_done_event, results):
    global count
    global driver
    global start
    driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(keyword)
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()
    reviews = []

    try:
        items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]'))
        )
        for item in items:
            try:
                title = item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')
            except:
                title = item.find_element(By.XPATH, './/span[@class="a-size-base-plus a-color-base a-text-normal"]')

            img_link = item.find_element(By.XPATH, './/img[@class="s-image"]').get_attribute('src')
            data_asin = item.get_attribute("data-asin")
            product_asin = data_asin
            break
    except Exception as e:
        logger.error(f"Error in after_func while getting items: {str(e)}")
        scraping_done_event.set()
        return

    web = "https://www.amazon.com/product-reviews/" + product_asin + "/"
    logger.info(f"Product Image Link: {img_link}")
    logger.info(f"Product Title: {title.text}")
    results[0] = title.text

    list_of_collections = dbase.list_collection_names()
    if title.text in list_of_collections:
        collection_name = dbase[title.text]
        # Assuming 'count' is the field you want to update
        filter_criteria = {}  # Provide a filter criteria based on your document structure

        # Update the 'count' field using $inc to increment the value
        update_result = collection_name.update_one(filter_criteria, {"$inc": {"count": 1}})

        if update_result.modified_count > 0:
            logger.info("Collection exists, count incremented")
            scraping_done_event.set()
            return title.text
        else:
            logger.warning("Collection exists, but count not updated")
    else:
        logger.info("Collection does not exist")
    count = 1
    collection_name = dbase[title.text]
    title_data = {"product_name": title.text, "product_img": img_link, "count": count}
    logger.info(f"Product Web Link: {web}")

    driver.get(web)
    captcha_solver()
    driver.get_screenshot_as_file("screenshot.png")
    driver.implicitly_wait(5)
    count = 1
    temp = 0
    insert = {}

    try:
        collection_name.insert_one(title_data)
        while True:
            items = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "a-row a-spacing-small review-data")]'))
            )
            for item in items:
                review = item.find_element(By.XPATH, './/span[@class="a-size-base review-text review-text-content"]')
                temp += 1
                insert = {"Review": review.text}
                collection_name.insert_one(insert)
                reviews.append(review.text)
                if temp > 14:
                    logger.info("Temp executed inner loop")
                    break

            if temp > 14:
                logger.info("Temp executed outer loop")
                break

            try:
                next_page = driver.find_element("xpath", "//li[contains(@class, 'a-last')]/a").get_attribute('href')
            except:
                logger.info("Page End")
                break

            count += 1
            logger.info(f"Page: {count}")
            driver.get(next_page)
            driver.implicitly_wait(2)
    except Exception as e:
        logger.error(f"Error in after_func while scraping reviews: {str(e)}")

    driver.quit()
    logger.info(reviews)
    end = time.time()
    logger.info(f"Total time: {end - start}")

    scraping_done_event.set()
    return title.text

# Example usage:
# get_reviews_amazon()
# after_func("lenovo thinkpad", scraping_done_event, results)
