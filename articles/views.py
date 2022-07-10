from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
from django.template.loader import render_to_string, get_template
from django.contrib.auth.decorators import login_required

from .forms import articles_form


def home(request):
    # obj = Article.objects.create(tittle="First Title",content="Hello Envirnoment")

    obj = Article.objects.get(id=1)
    lst = Article.objects.all()

    context = {
        "t": obj.tittle,
        "i": obj.id,
        "c": obj.content,
        "l": lst,
    }

    HTML_String = render_to_string("index.html", context=context)
    return HttpResponse(HTML_String)


def article(request, article_id):
    art = Article.objects.get(id=article_id)
    context = {"a": art}
    cont = render_to_string("articles.html", context=context)
    return HttpResponse(cont)


def search(request):
    que = request.GET['q']
    print(que)
    try:
        art = Article.objects.get(id=que)
    except:
        art = ""
    context = {"a": art}
    return render(request, 'search.html', context)


@login_required(login_url='/accounts/')
def create(request):
    d = articles_form()
    contex = {
        "forms": d

    }

    if request.method == "POST":
        form = articles_form(request.POST or None)
        contex['forms'] = form
        if form.is_valid():
            article = form.save()
            contex["art"] = article
            contex["created"] = True
            return render(request, "created.html", contex)

    return render(request, "create.html", contex)


def created(request):
    contex = {}
    pass

    

    
