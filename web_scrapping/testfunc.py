from text import *
import threading

thread_one = threading.Thread(target=get_reviews_amazon())
thread_two = threading.Thread(target=after_func("the north face jacket"))

thread_one.start()
thread_two.start()
