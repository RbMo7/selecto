from .reviews_scrap import *
import threading


def scrap(keyword):
    # Create a list to store the results
    results = [None]

    # Create an event to signal when the scraping is done
    scraping_done = threading.Event()

    thread_one = threading.Thread(target=get_reviews_amazon())
    thread_two = threading.Thread(target=after_func, args=("mamaearth face", scraping_done, results))

    thread_one.start()
    thread_two.start()

    # Wait for both threads to finish
    thread_two.join()

    # Retrieve the result from the list
    value = results[0]
    print("Scraping result:", value)
    return value
