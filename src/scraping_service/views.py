from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now().date()
    name = 'Sergey'
    data_text = {'date': date, 'name': name}
    return render(request, 'home.html', data_text)
