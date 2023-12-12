# scraping_utils.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from amazoncaptcha import AmazonCaptcha
from django.http import JsonResponse
from .models import AmazonReview  # Import the model

def scrape_reviews(search_text):
    web = 'https://www.amazon.com'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(web)

    try:
        img_div = driver.find_element(By.XPATH, "//div[@class = 'a-row a-text-center']//img").get_attribute('src')
        captcha = AmazonCaptcha.fromlink(img_div)
        captcha_value = AmazonCaptcha.solve(captcha)
        input_field = driver.find_element(By.ID, "captchacharacters").send_keys(captcha_value)
        button = driver.find_element(By.CLASS_NAME, "a-button-text")
        button.click()
    except Exception as captcha_error:
        print("Captcha solving error:", captcha_error)
        return JsonResponse({'error': 'Captcha solving failed'})

    next_page = ''
    driver.implicitly_wait(5)
    keyword = "mac m1 apple"
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
        data_asin = item.get_attribute("data-asin")
        product_asin = data_asin
        break
    print(product_asin)
    web = "https://www.amazon.com/product-reviews/" + product_asin + "/"
    print(web)
    driver.get(web)
    driver.implicitly_wait(5)
    count=1
    while True:
        items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "a-row a-spacing-small review-data")]')))
        for item in items:
            review = item.find_element(By.XPATH, './/span[@class="a-size-base review-text review-text-content"]')
            reviews.append(review.text)
        try:
            next_page = driver.find_element("xpath","//li[contains(@class, 'a-last')]/a").get_attribute('href')
        except:
            print("Page End")
            break
        count += 1
        print("Page:",count)
        driver.get(next_page)
        driver.implicitly_wait(5)

    driver.quit()
    print(reviews)