from text import *
import threading

def scrap(keyword):
    thread_one = threading.Thread(target=get_reviews_amazon())
    thread_two = threading.Thread(target=after_func(keyword))

    thread_one.start()
    thread_two.start()
