from django.shortcuts import render

def index(request):
    data = "current data"

    context = {
        "data": data
    }

    return render(request, 'app/index.html',context)