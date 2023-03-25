from django.shortcuts import render, redirect
from .models import articles
from .forms import articlesForm


def news_home(request):
    news = articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = articlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'

    form = articlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html')
