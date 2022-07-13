from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def hello(request):
    return HttpResponse('<h1>Hello world</h1>')

def homepage(request):
    products = Product.objects.all()
    allProducts = []
    column = []
    for i, p in enumerate(products, start=1):
        if i % 3 == 0:
            column.append(p)
            allProducts.append(column)
            column = []
        else:
            column.append(p)
    if len(column) != 0:
        allProducts.append(column)
    context = {'allProducts': allProducts, 'column': column}
    return render(request, 'python/home.html', context)

def contactpage(request):
    if request.method == 'POST':
        data = request.POST.copy()
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')

        # save data to database
        newContact = ContactList()
        newContact.email = email
        newContact.title = title
        newContact.detail = detail
        newContact.save()
    return render(request, 'python/contact.html')