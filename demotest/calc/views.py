from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = float(data.get('a', 0))
            b = float(data.get('b', 0))
            result = a + b
            return JsonResponse({'operation': 'add', 'result': result})
        except:
            return JsonResponse({'error': 'Invalid input'}, status=400)

@csrf_exempt
def subtract(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = float(data.get('a', 0))
            b = float(data.get('b', 0))
            result = a - b
            return JsonResponse({'operation': 'subtract', 'result': result})
        except:
            return JsonResponse({'error': 'Invalid input'}, status=400)

@csrf_exempt
def multiply(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = float(data.get('a', 0))
            b = float(data.get('b', 0))
            result = a * b
            return JsonResponse({'operation': 'multiply', 'result': result})
        except:
            return JsonResponse({'error': 'Invalid input'}, status=400)

@csrf_exempt
def divide(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = float(data.get('a', 0))
            b = float(data.get('b', 0))
            if b == 0:
                return JsonResponse({'error': 'Division by zero'}, status=400)
            result = a / b
            return JsonResponse({'operation': 'divide', 'result': result})
        except:
            return JsonResponse({'error': 'Invalid input'}, status=400)
