from django.shortcuts import render
from .models import News
# Create your views here.

def home_view(request):
    qs = News.objects.all()
    return render(request, 'scraping/home.html', {'object_list': qs})