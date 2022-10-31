from django.shortcuts import render
from django.utils.datetime_safe import datetime
from datetime import datetime
# Create your views here.

# now = datetime.datetime.now()
def index(request):
    content = {
        'title': 'Geegshop',
        # 'time' : now
    }

    return render(request, 'mainapp/index.html', content)




def products(request):
    categories = [
        {'name': 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксессуары'},
        {'name': 'Подарки'},
    ]

    content = {
        'title': 'Geegshop - Каталог',
        'categories': categories,
        # 'time': now
    }

    return render(request, 'mainapp/products.html', content)
