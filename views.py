from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import YourModel  # Import your model(s) if needed

def index(request):
    """
    A simple view that renders an HTML template.
    """
    return render(request, 'your_app/index.html')

def get_data(request):
    """
    A view that returns data as JSON.
    """
    data = {
        'message': 'Hello, World!',
        'count': 42,
    }
    return JsonResponse(data)

# You can define more views as needed based on your project's requirements
