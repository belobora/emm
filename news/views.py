from django.shortcuts import render, redirect
from .models import Art
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(req):
    # news = Art.objects.all()
    news = Art.objects.order_by('title')  # или минус или -date [:-1]
    return render(req, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Art
    template_name = 'news/details_view.html'
    context_object_name = 'artic'

class NewsDeleteView(DeleteView):
    model = Art
    template_name = 'news/news-delete.html'
    success_url = '/news/'


class NewsUpdateView(UpdateView):
    model = Art
    template_name = 'news/create.html'

   # fields = ["title", 'anon', 'full', 'date']
    form_class = ArticlesForm

def create(req):
    error = ''
    if req.method == 'POST':
        form = ArticlesForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма неправильная'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(req, 'news/create.html', data)
