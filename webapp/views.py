import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calculation(request, *args, **kwargs):
    if request.method == 'POST':
        numbers = json.loads(request.body)
        try:
            a = int(numbers.get("A"))
            b = int(numbers.get("B"))
            if request.path == '/add/':
                answer = {"answer": a + b}
                return JsonResponse(answer)

            if request.path == '/subtract/':
                answer = {"answer": a - b}
                return JsonResponse(answer)

            if request.path == '/multiply/':
                answer = {"answer": a * b}
                return JsonResponse(answer)

            if request.path == '/divide/':
                if b != 0:
                    answer = {"answer": a / b}
                    return JsonResponse(answer)
                response = JsonResponse({'error': 'Division by zero!'})
                response.status_code = 400
                return response
        except ValueError:
            response = JsonResponse({"error": "Error! Please enter numbers"})
            response.status_code = 400
            return response
    response = JsonResponse({'error': 'Only POST method allowed!'})
    return response


def index_view(request):
    return render(request=request, template_name='index.html')
