# from celery import shared_task
# from .utils import fetch_part_info  # Импорт вашей функции парсинга

# @shared_task
# def fetch_part_info_task(article):
#     try:
#         # Вызов функции парсинга для получения данных
#         result = fetch_part_info(article)

#         if result:
#             # Упакуем результат в список, чтобы соответствовать ожидаемому формату
#             return [result]
#         else:
#             return []  # Если данные не найдены, вернем пустой список
#     except Exception as e:
#         # Логгирование ошибки для отладки
#         return {"error": str(e)}
from celery import shared_task
from .utils import fetch_part_info  # Импортируем функцию, а не задачу

@shared_task
def fetch_part_info_task(article):
    """
    Задача Celery для получения информации о запчасти с сайта.
    """
    try:
        # Вызов функции парсинга для получения данных
        results = fetch_part_info(article)  # Исправлено: вызывается функция из utils

        # Если парсинг успешен, возвращаем результаты
        if results:
            return results  # Результаты уже в виде списка словарей
        else:
            # Если данные не найдены, возвращаем пустой список
            return []
    except Exception as e:
        # Если произошла ошибка, логируем и возвращаем её в ответе
        return {"error": f"Ошибка при обработке данных: {str(e)}"}
