from celery import shared_task
from parts.utils import fetch_part_info  # Используем функцию для поиска

@shared_task
def search_spare_part(article):
    """
    Главный таск для поиска запчастей.
    """
    return fetch_part_info(article)
