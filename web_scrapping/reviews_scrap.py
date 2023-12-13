from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from amazoncaptcha import AmazonCaptcha
from database import get_database
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time



def get_reviews_amazon(keyword):
    start = time.time()
    dbase = get_database()
    web = 'https://www.amazon.com'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
        }
    )
    ##captcha solver
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disk-cache-dir=/path/to/cache')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    def captchaSolver():
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
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(web)
    captchaSolver()
    next_page = ''
    driver.implicitly_wait(2)
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
        try:
            title = item.find_element(By.XPATH,'.//span[@class="a-size-medium a-color-base a-text-normal"]')
        except:
            title = item.find_element(By.XPATH,'.//span[@class="a-size-base-plus a-color-base a-text-normal"]')
        img_link = item.find_element(By.XPATH,'.//img[@class="s-image"]').get_attribute('src')
        data_asin = item.get_attribute("data-asin")
        product_asin = data_asin
        break
    web = "https://www.amazon.com/product-reviews/" + product_asin + "/"
    print(img_link)
    print(title.text)
    list_of_collections = dbase.list_collection_names()
    # print(list_of_collections)
    if title.text in list_of_collections:
        print("Collection exists")
        collection = dbase[title.text]
        cursor = collection.find({})
        for doc in cursor:
            reviews.append(doc)
        while True:
            try:
                # print(reviews_arr[i]['Review'])
                overall = overall + reviews[i]['Review']
                i = i + 1
            except:
                break
        reviews = overall
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
    print(web)
    driver.get(web)
    captchaSolver()
    # driver.get_screenshot_as_file("screenshot.png")
    driver.implicitly_wait(5)
    count=1
    temp = 0
    insert = {}
    try:
        collection_name.insert_one(title)
        while True:
            items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "a-row a-spacing-small review-data")]')))
            for item in items:
                review = item.find_element(By.XPATH, './/span[@class="a-size-base review-text review-text-content"]')
                temp += 1
                insert ={"Review":review.text}
                # print("No of reveiws:", temp)
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
            driver.implicitly_wait(2)
    except:
        print("No reviews found")
    driver.quit()
    print(reviews)
    end = time.time()
    print("Total time is: ", end - start)

print("the result is", get_reviews_amazon("marker"))
