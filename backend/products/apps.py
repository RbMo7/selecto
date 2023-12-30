from django.apps import AppConfig
# from .scraping import scraping_thread


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    
    # def ready(self):
    #     # Ensure the scraping thread is running when the app is loaded
    #     if not scraping_thread.is_alive():
    #         scraping_thread.start()