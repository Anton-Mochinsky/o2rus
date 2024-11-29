from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import fetch_part_info_task
from django.shortcuts import render
from parts.utils import fetch_part_info

class FetchPartInfoView(APIView):
    def post(self, request, *args, **kwargs):
        article = request.data.get("article")
        if not article:
            return Response(
                {"status": "error", "message": "Article is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Синхронный вызов задачи
        result = fetch_part_info_task.apply(args=[article])
        
        if result.successful():
            # Если задача успешно выполнена, возвращаем её результат
            return Response(
                {"status": "success", "data": result.result},
                status=status.HTTP_200_OK
            )
        else:
            # Если задача завершилась с ошибкой
            return Response(
                {"status": "error", "message": "Task failed"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def search_parts(request):
    """
    Вьюха для обработки поиска запчастей.
    """
    results = None
    error = None

    if request.method == 'POST':
        article = request.POST.get('article')
        if article:
            data = fetch_part_info(article)
            if 'error' in data:
                error = data['error']
            else:
                results = data
        else:
            error = "Пожалуйста, введите артикул."

    return render(request, 'parts/search.html', {'results': results, 'error': error})
