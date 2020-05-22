"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Post

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {'title':'Home Page','year':datetime.now().year, 'posts': Post.objects.all()}
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def classes(request):
    """Renders the classes page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/classes.html',
        {
            'title':'لیست کلاس‌ها',
            'message':'در این قسمت، لیست کلاس‌های ایجادشده نمایش داده میشود',
            'year':datetime.now().year,
        }
    )

def profs(request):
    """Renders the profs page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profs.html',
        {
            'title':'اساتید',
            'message':'در این صفحه، لیست اساتید ثبت‌شده در سیستم نمایش داده میشوند',
            'year':datetime.now().year,
        }
    )
