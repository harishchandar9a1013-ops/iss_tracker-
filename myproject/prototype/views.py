import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def iss_tracker(request):
    iss_url = "http://api.open-notify.org/iss-now.json"
    astro_url = "http://api.open-notify.org/astros.json"

    iss_data = requests.get(iss_url).json()
    astro_data = requests.get(astro_url).json()

    context = {
        'lat': iss_data['iss_position']['latitude'],
        'lon': iss_data['iss_position']['longitude'],
        'people': astro_data['people'],
        'count': astro_data['number'],
    }
    return render(request, 'index.html', context)

def iss_position(request):
    data = requests.get("http://api.open-notify.org/iss-now.json").json()
    return JsonResponse({
        'lat': data['iss_position']['latitude'],
        'lon': data['iss_position']['longitude'],
    })