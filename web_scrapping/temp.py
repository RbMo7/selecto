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


def initial_load():
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