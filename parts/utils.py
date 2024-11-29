import requests
from bs4 import BeautifulSoup

def fetch_part_info(article):
    """
    Получение информации о запчастях с сайта comtt.ru.
    """
    login_url = "https://www.comtt.ru/login.php"
    search_url = f"https://www.comtt.ru/search.php?fnd={article}"
    credentials = {'login': 'caraterra', 'pass': '116116'}

    session = requests.Session()
    try:
        # Авторизация
        login_response = session.post(login_url, data=credentials)
        print("Login status:", login_response.status_code)
        if "неверный логин или пароль" in login_response.text.lower():
            return {"error": "Ошибка авторизации. Проверьте учетные данные."}

        # Поиск
        response = session.get(search_url)
        print("Search page status:", response.status_code)
        if response.status_code != 200:
            return {"error": f"Ошибка доступа к странице поиска: {response.status_code}"}

        soup = BeautifulSoup(response.text, 'html.parser')

        # Парсинг результатов
        results = []

        # Получаем все товары
        items = soup.select(f'tr[price][art="{article}"]')

        # Преобразуем данные из всех строк в список с количествами
        quantities = []
        for item in items:
            quantity_elem = item.select_one('td[cell_id="count"]')
            if quantity_elem:
                quantity_text = quantity_elem.get_text(strip=True)
                quantity = int(quantity_text.split()[0])  # Преобразуем количество в целое число
                quantities.append(quantity)

        # Если первое количество равно сумме всех остальных
        if quantities and quantities[0] == sum(quantities[1:]):
            items = items[1:]  # Убираем первую строку

        # Проходим по оставшимся товарам и собираем информацию
        for item in items:
            delivery_date_elem = item.select_one('td[class="time"]')
            quantity_elem = item.select_one('td[cell_id="count"]')

            quantity = 0
            if quantity_elem:
                quantity_text = quantity_elem.get_text(strip=True)
                quantity = int(quantity_text.split()[0])

            results.append({
                "article": item.get('art', 'Нет данных'),
                "quantity": quantity,
                "price": float(item.get('price', 0)),
                "delivery_date": delivery_date_elem.text.strip() if delivery_date_elem else "Нет данных",
                "delivery_time": delivery_date_elem.get('tooltip') if delivery_date_elem else "Нет данных",
                "link": f"http://www.comtt.ru/search.php?fnd={article}"  # Ссылка на товар
            })

        return results

    except Exception as e:
        return {"error": f"Ошибка выполнения задачи: {str(e)}"}
