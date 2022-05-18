from zlib import DEF_BUF_SIZE
import unicodedata
import requests
from django.db.models import Q
from .forms import ArticleForm
from .models import cliente
from re import X
import django
from django.shortcuts import redirect, render
from sqlalchemy import false, true
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", ".settings")
django.setup()
#from proyecto.core.admin import articleResourse
# Create your views here.


def home(request):
    clientes = cliente.objects.all()

    data = {
        'clientes': clientes
    }

    return render(request, 'core/home.html', data)


def createArticle(request):
    if request.method == 'GET':
        clientes = cliente.objects.all()

        form = ArticleForm()
        data = {
            'form': form
        }
    else:
        form = ArticleForm(request.POST)
        data = {
            'form': form
        }
    if form.is_valid():
        # p = article()
        p = form.save()
        id = p.id

        return redirect('home')

    return render(request, 'core/createArticle.html', data)


def editArticle(request, id):
    clientes = cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ArticleForm(instance=clientes)
        data = {
            'form': form
        }
    else:
        form = ArticleForm(request.POST, instance=clientes)
        data = {
            'form': form
        }
        if form.is_valid():
            p = form.save()
            id = p.id

            return redirect('home')

    return render(request, 'core/createArticle.html', data)


def eraseArticle(request, id):
    clientes = cliente.objects.get(id=id)

    clientes.delete()
    return redirect('home')
