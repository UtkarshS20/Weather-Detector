from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method=='POST':
        city = request.POST['city']
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=6fe143130fe7c29a58527be0e5a8d181').read()
        json_data=json.loads(res)
        data= {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'])+ ' ' +str(json_data['coord']['lat']),
            'description': (json_data['weather'][0]['description']),
            'temp': str(json_data['main']['temp']),
            'feels_like': str(json_data['main']['feels_like']),
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        city=''
        data={}
    return render (request,'index.html',{'city': city, 'data': data})