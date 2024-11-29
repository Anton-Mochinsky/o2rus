from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установить настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spare_part_finder.settings')

# Создать экземпляр приложения Celery
app = Celery('spare_part_finder')

# Загрузить конфигурацию из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживать задачи в приложениях
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
