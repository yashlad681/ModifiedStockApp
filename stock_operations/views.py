from django.shortcuts import render
import requests
import json
from .models import SearchLog


def home(request):
    if request.method=='POST':
        stock_name=request.POST['name']
        api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{stock_name}/quote?token=pk_8b445b4f633944e88fed24aacf86fed9")
        api_graph_response = requests.get(f"https://cloud.iexapis.com/stable/stock/{stock_name}/chart/1m?chartByDay=true&range=1m&token=pk_8b445b4f633944e88fed24aacf86fed9")
        api_logo_response = requests.get(f"https://cloud.iexapis.com/stable/stock/{stock_name}/logo?token=pk_8b445b4f633944e88fed24aacf86fed9")
        try:         
            graph_data = json.loads(api_graph_response.content)
            api_logo_response = json.loads(api_logo_response.content)
            labels = []
            prices = []
            for item in graph_data:
                labels.append(item.get('date'))
                prices.append(item.get('close'))
        except Exception as e:
            api_logo_response = None
            graph_data= None
            labels = None
            prices = None
        try:
            api_response=json.loads(api_request.content)
            SearchLog.objects.create(stock_name=stock_name)
        except Exception as e:
            api_response= None
        return render(request, 'home.html',{"data":api_response,'labels':labels,'prices':prices, 'logo':api_logo_response})
    else:
        return render(request, 'home.html',{"name":"Enter stock symbol above."})

def recently_searched_stocks(request):
    history = SearchLog.objects.all()
    return render(request, 'home.html',{"history":history})
