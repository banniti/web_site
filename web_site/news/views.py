from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailViews(DetailView):
    model = News
    template_name = 'news/details_news.html'
    context_object_name = 'news'

class NewsUpdateViews(UpdateView):
    model = News
    template_name = 'news/create.html'
    form_class = NewsForm


class NewsDeleteViews(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма не верная'

    form = NewsForm()
    data = {'form': form,
            'error': error
            }
    return render(request, 'news/create.html', data)

