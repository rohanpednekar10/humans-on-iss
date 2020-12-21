from django.shortcuts import render
import requests

# Create your views here.
def read_index(request):
    response = requests.get('http://api.open-notify.org/astros.json').json()
    context = {
        'number': response['number'],
        'people': response['people'],
    }
    return render(request, 'app/base.html', context)