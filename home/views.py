from django.conf import settings
from django.shortcuts import render

# Create your views here.

def index(request):
    # Render the index page while passing MEDIA_URL
    return render(request, 'home/index.html', {'MEDIA_URL': settings.MEDIA_URL})

# If you have another view, ensure it does the same if needed
def base_view(request):
    return render(request, 'base.html', {'MEDIA_URL': settings.MEDIA_URL})