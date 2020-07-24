from django.shortcuts import render
import requests
import json
def news(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=e8381387b9984e25bad3016eb98d885d')
    response_json = json.loads(news_api_request.content)

    return render(request, 'news.html', {'response_json' : response_json})

# Create your views here.
